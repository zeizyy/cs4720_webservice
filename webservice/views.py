from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from webservice.forms import UserForm, LoginForm, EventForm, EventEditForm, TodoEditForm
from webservice.models import User, Authenticator, Event, Todo
from django.contrib.auth import hashers
from django.forms.models import model_to_dict
import base64, os, uuid
import datetime

error_post = 'only post request is accepted.'
error_get = 'only get request is accepted.'
missing_field = 'form not valid.'
auth_invalid = 'invalid authenticator'
user_not_exist = 'user not exit'
# Create your views here.
def index(request):
	return _success_response(request,'index page of the webservice for cs4720 final project.')

def create_user(request):
	post = _check_post(request)
	if not post:
		return _error_response(request, error_post)
	user_form = UserForm(post)
	if user_form.is_valid():
		user = user_form.save()
	else:
		return _error_response(request, user_form.errors)
	authenticator = _create_authenticator(user.id)
	rsp = {'user_id':user.id, 'authenticator':authenticator}
	return _success_response(request,rsp)

def login(request):
	post = _check_post(request)
	if not post:
		return _error_response(request, error_post)
	login_form = LoginForm(post)
	if not login_form.is_valid():
		return _error_response(request, login_form.errors)
	username = post['username']
	password = post['password']
	user = _get_user_by_username(request, username)
	if not user:
		return _error_response(request, user_not_exist)
	is_correct = hashers.check_password(password, user.password)
	if is_correct:
		authenticator = _create_authenticator(user.id)
		return _success_response(request, {"user_id":user.id, "authenticator":authenticator})
	else:
		return _error_response(request, "Logins do not match.")

def logout(request):
	post = _check_post(request)
	if not post:
		return _error_response(request, error_post)
	if 'authenticator' not in post:
		return _error_response(request, missing_field)
	authenticator = post['authenticator']
	try:
		auth = Authenticator.objects.get(authenticator = authenticator)
		auth.delete()
		return _success_response(request)
	except:
		return _error_response(request)

def create_event(request):
	post =_check_post(request)
	if not post:
		return _error_response(request, error_post)
	event_form = EventForm(post)
	if not event_form.is_valid():
		return _error_response(request, event_form.errors)
	event = event_form.save(commit=False)
	authenticator = post['authenticator']
	user_id = _validate(request, authenticator)
	if not user_id:
		return _error_response(request, auth_invalid)
	user = _get_user_by_id(request, user_id)
	if not user:
		return _error_response(request, user_not_exist)
	event.user = user
	# event.UUID = str(uuid.uuid4())
	# try:
	event.save()
	# except:
	# 	return _error_response(request, 'event cannot be saved')
	return _success_response(request,{"uuid":event.UUID})

def edit_event(request):
	post =_check_post(request)
	if not post:
		return _error_response(request, error_post)
	
	
	# event = event_form.save(commit=False)
	uuid = post['UUID']
	try:
		event = Event.objects.get(UUID=uuid)
	except:
		return _error_response(request, "event does not exist")
	authenticator = post['authenticator']
	user_id = _validate(request, authenticator)
	if not user_id:
		return _error_response(request, auth_invalid)

	event_form = EventEditForm(post, instance=event)
	if not event_form.is_valid():
		return _error_response(request, event_form.errors)
	event_form.save()
	return _success_response(request,{"uuid":event.UUID})

def get_all_event(request):
	post = _check_post(request)
	if not post:
		return _error_response(request, error_post)
	valid_input = 'authenticator' in post
	if not valid_input:
		return _error_response(request, missing_field)
	authenticator = post['authenticator']
	user_id = _validate(request, authenticator)
	if not user_id:
		return _error_response(request, auth_invalid)
	user = _get_user_by_id(request, user_id)
	if not user:
		return _error_response(request, user_not_exist)
	events = Event.objects.filter(user=user)
	events = list(map(model_to_dict, events))
	for event in events:
		start_time = event['start_time']
		event['start_time'] = to_normal(start_time)
		end_time = event['end_time']
		event['end_time'] = to_normal(end_time)
	return _success_response(request, events)

def to_normal(tztime):
	tztime = str(tztime)
	date = tztime[:10]
	time = tztime[11:19]
	return date+" "+time

def get_all_todo(request):
	post = _check_post(request)
	if not post:
		return _error_response(request, error_post)
	valid_input = 'authenticator' in post
	if not valid_input:
		return _error_response(request, missing_field)
	authenticator = post['authenticator']
	user_id = _validate(request, authenticator)
	if not user_id:
		return _error_response(request, auth_invalid)
	user = _get_user_by_id(request, user_id)
	if not user:
		return _error_response(request, user_not_exist)
	todos = Todo.objects.filter(user=user)
	todos = list(map(model_to_dict, todos))
	for todo in todos:
		start_time = todo['due_datetime']
		todo['due_datetime'] = to_normal(start_time)
		end_time = todo['reminder_datetime']
		todo['reminder_datetime'] = to_normal(end_time)
	return _success_response(request, todos)

def purge_todo(request):
	post = _check_post(request)
	if not post:
		return _error_response(request, error_post)
	valid_input = 'authenticator' in post
	authenticator = post['authenticator']
	user_id = _validate(request, authenticator)
	if not user_id:
		return _error_response(request, auth_invalid)
	todos = Todo.objects.all()
	for todo in todos:
		todo.delete()
	return _success_response(request, "success")

def sync_event(request):
	post = _check_post(request)
	if not post:
		return _error_response(request, error_post)
	edit_form = EventEditForm(post)
	if not edit_form.is_valid():
		return _error_response(request, edit_form.errors)
	valid_input = 'authenticator' in post
	authenticator = post['authenticator']
	user_id = _validate(request, authenticator)
	if not user_id:
		return _error_response(request, auth_invalid)
	user = _get_user_by_id(request, user_id)
	uuid = post["UUID"]
	try:
		event = Event.objects.get(UUID=uuid)
		# return _success_response(request, model_to_dict(event))
		event_form = EventEditForm(post, instance=event)
	except:
		event_form = EventEditForm(post)
		# return HttpResponse(post)
	event = event_form.save(commit=False)
	event.user = user
	event.created = datetime.datetime.now()
	event.UUID = uuid
	event.save()
	return _success_response(request, event.UUID)

def sync_todo(request):
	post = _check_post(request)
	if not post:
		return _error_response(request, error_post)
	edit_form = TodoEditForm(post)
	if not edit_form.is_valid():
		return _error_response(request, edit_form.errors)
	valid_input = 'authenticator' in post
	authenticator = post['authenticator']
	user_id = _validate(request, authenticator)
	if not user_id:
		return _error_response(request, auth_invalid)
	user = _get_user_by_id(request, user_id)
	uuid = post["UUID"]
	try:
		todo = Todo.objects.get(UUID=uuid)
		# return _success_response(request, model_to_dict(event))
		todo_form = TodoEditForm(post, instance=todo)
	except:
		todo_form = TodoEditForm(post)
		# return HttpResponse(post)
	todo = todo_form.save(commit=False)
	todo.user = user
	todo.created = datetime.datetime.now()
	todo.UUID = uuid
	todo.save()
	return _success_response(request, todo.UUID)

def error(request):
	return _error_response(request, 'api does not exist.')

def _get_event(request, event_id):
	pass

def _get_user_by_id(request, user_id):
	try:
		user = User.objects.get(pk=user_id)
		return user
	except:
		return False

def _get_user_by_username(request, username):
	try:
		user = User.objects.get(username=username)
		return user
	except:
		return False

def _validate(request, authenticator):
	try:
		auth = Authenticator.objects.get(authenticator = authenticator)
		return auth.user_id
	except:
		return False

def _check_post(request):
	if not request.method == 'POST':
		return False
	return request.POST

def _create_authenticator(user_id):
	try:
		auth = Authenticator.objects.get(user_id=user_id)
		return auth.authenticator
	except:
		pass
	authenticator =	base64.b64encode(os.urandom(32)).decode('utf-8')
	auth = Authenticator(authenticator=authenticator, user_id=user_id)
	auth.save()
	return authenticator

def _error_response(request, error = None):
	if isinstance(error, str):
		error = {"single_error":error}
	return JsonResponse({'ok': False, 'error':error})

def _success_response(request, rsp = None):
	return JsonResponse({'ok':True, 'rsp':rsp})


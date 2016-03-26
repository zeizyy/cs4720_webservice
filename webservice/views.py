from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from webservice.forms import UserForm
from webservice.models import User, Authenticator, Event
from django.contrib.auth import hashers
import base64, os

error_post = 'only post request is accepted.'
error_get = 'only get request is accepted.'
missing_field = 'form not valid.'
auth_invalid = 'invalid authenticator'
user_not_exist = 'user not exit'
# Create your views here.
def index(request):
	return _success_response(request,'index page of the webservice for cs4720 final project.')

def create_user(request):
	_check_post(request)
	user_form = UserForm(request.POST)
	if user_form.is_valid():
		user = user_form.save()
	else:
		return _error_response(request, missing_field)
	authenticator = _create_authenticator(user.id)
	rsp = {'user_id':user.id, 'authenticator':authenticator}
	return _success_response(request,rsp)

def login(request):
	_check_post(request)
	post = request.POST
	valid_input = 'username' in post and 'password' in post
	if not valid_input:
		return _error_response(request, missing_field)
	username = post['username']
	password = post['password']
	try:
		user = User.objects.get(username = username)
	except:
		return _error_response(request, "User not found.")
	is_correct = hashers.check_password(password, user.password)
	if is_correct:
		authenticator = _create_authenticator(user.id)
		return _success_response(request, {"user_id":user.id, "authenticator":authenticator})
	else:
		return _error_response(request, "Username and password do not match.")

def logout(request):
	_check_post(request)
	post = request.POST
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
	valid_input = 'name' in post and 'authenticator' in post
	if not valid_input:
		return _error_response(request, missing_field)
	name = post['name']
	authenticator = post['authenticator']

	user_id = _validate(request, authenticator)
	user = _get_user(request, user_id)
	event = Event(name=name, user=user)
	try:
		event.save()
	except:
		return _error_response(request, 'cannot save event')
	return _success_response(request)

def get_all_event(request):
	post = _check_post(request)
	valid_input = 'authenticator' in post
	if not valid_input:
		return _error_response(request, missing_field)
	authenticator = post['authenticator']
	user_id = _validate(request, authenticator)
	user = _get_user(request, user_id)
	events = Event.objects.filter(user=user)
	rsp = {'events':[]}
	for event in events:
		e = {'name':event.name, 'last_modified':event.last_modified}
		rsp['events'].append(e)
	return _success_response(request, rsp)

def error(request):
	return _error_response(request, 'api not exist.')

def _get_event(request, event_id):
	pass

def _get_user(request, user_id):
	try:
		user = User.objects.get(pk=user_id)
		return user
	except:
		return _error_response(request, user_not_exist)


def _validate(request, authenticator):
	try:
		auth = Authenticator.objects.get(authenticator = authenticator)
		return auth.user_id
	except:
		return _error_response(request, auth_invalid)


def _check_post(request):
	if not request.method == 'POST':
		return _error_response(request, error_post)
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

def _error_response(request, error_msg = None):
	return JsonResponse({'ok': False, 'error':error_msg})

def _success_response(request, rsp = None):
	return JsonResponse({'ok':True, 'rep':rsp})
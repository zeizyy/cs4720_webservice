from django import forms
from webservice.models import User, Event, Todo


class UserForm(forms.ModelForm):
	class Meta:
		model = User
		# fields = ['username', 'password']
		exclude = []

class LoginForm(forms.Form):
	username = forms.CharField(max_length=24)
	password = forms.CharField(max_length=96)

class EventForm(forms.ModelForm):
	authenticator = forms.CharField(max_length=96)
	class Meta:
		model = Event
		exclude = ['user']

class EventEditForm(forms.ModelForm):
	authenticator = forms.CharField(max_length=96)
	UUID = forms.CharField(max_length=96)
	class Meta:
		model = Event
		exclude = ['UUID','user']

class TodoEditForm(forms.ModelForm):
	authenticator = forms.CharField(max_length=96)
	UUID = forms.CharField(max_length=96)
	class Meta:
		model = Todo
		exclude = ['UUID','user']
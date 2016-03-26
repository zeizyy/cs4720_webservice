from django import forms
from webservice.models import User


class UserForm(forms.ModelForm):
	class Meta:
		model = User
		# fields = ['username', 'password']
		exclude = []




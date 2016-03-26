from django.db import models
from django.contrib.auth import hashers
import datetime
# Create your models here.

class User(models.Model):
	username = models.CharField(max_length=24, unique=True)
	password = models.CharField(max_length=96)

	def save(self, *args, **kwargs):
		password = hashers.make_password(self.password)
		self.password = password
		super(User, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.username

class Authenticator(models.Model):
	authenticator = models.CharField(max_length=100, primary_key=True)
	user_id = models.IntegerField()
	date_created = models.DateTimeField(default=datetime.datetime.now)

	def __unicode__(self):
		return str(self.user_id)

class Event(models.Model):
	name = models.CharField(max_length=100)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	last_modified = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.name

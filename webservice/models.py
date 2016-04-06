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

    def __str__(self):
        return self.username


class Authenticator(models.Model):
    authenticator = models.CharField(max_length=100, primary_key=True)
    user_id = models.IntegerField()
    date_created = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return str(self.user_id)


class Event(models.Model):
    UUID = models.CharField(max_length=36, primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Todo(models.Model):
    UUID = models.CharField(max_length=36, primary_key=True)
    name = models.CharField(max_length=100)
    note = models.CharField(max_length=200)
    due_datetime = models.DateTimeField()
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


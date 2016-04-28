from django.contrib import admin
from webservice.models import User, Authenticator, Event, Todo
# Register your models here.
admin.site.register(User)
admin.site.register(Authenticator)
admin.site.register(Event)
admin.site.register(Todo)
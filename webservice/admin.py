from django.contrib import admin
from webservice.models import User, Authenticator, Event
# Register your models here.
admin.site.register(User)
admin.site.register(Authenticator)
admin.site.register(Event)
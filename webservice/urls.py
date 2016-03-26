from django.conf.urls import include, url
from webservice import views

urlpatterns = [
    url(r'^$', views.index, name='Index'),
    url(r'^create_user/$', views.create_user, name = 'CreateUser'),
    url(r'^login/$', views.login, name = 'Login'),
    url(r'^logout/$', views.logout, name = 'Logout'),
    url(r'^events/new/$', views.create_event, name = 'CreateEvent'),
    url(r'^events/$', views.get_all_event, name = 'GetAllEvents'),
    url(r'^', views.error, name = 'Error'),
]

from django.conf.urls import include, url
from webservice import views

urlpatterns = [
    url(r'^$', views.index, name='Index'),
    url(r'^user/new/$', views.create_user, name = 'CreateUser'),
    url(r'^user/login/$', views.login, name = 'Login'),
    url(r'^user/logout/$', views.logout, name = 'Logout'),
    url(r'^events/new/$', views.create_event, name = 'CreateEvent'),
    url(r'^events/edit/$', views.edit_event, name = 'EditEvent'),
    url(r'^events/sync/$', views.sync_event, name = 'SyncEvent'),
    url(r'^events/$', views.get_all_event, name = 'GetAllEvents'),
    url(r'^todos/sync/$', views.sync_todo, name = 'SyncTodo'),
    url(r'^todos/purge/$', views.purge_todo, name = 'PurgeTodo'),
    url(r'^todos/$', views.get_all_todo, name = 'GetAllTodos'),
    url(r'^', views.error, name = 'Error'),
]

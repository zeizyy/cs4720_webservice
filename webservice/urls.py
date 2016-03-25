from django.conf.urls import include, url
from webservice import views

urlpatterns = [
    url(r'^$', views.index, name='Index'),
]

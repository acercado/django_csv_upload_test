from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^uploadtest/$', views.uploadtest, name='uploadtest'),
]
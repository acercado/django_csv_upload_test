from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^uploadtest/$', views.uploadtest, name='uploadtest'),
	url(r'^uploadtest2/$', views.uploadtest2, name='uploadtest2'),
]
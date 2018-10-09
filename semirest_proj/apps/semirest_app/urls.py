from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^users$', views.index),
    url(r'^users/new$', views.new),
    url(r'^users/(?P<user_id>\d+)$', views.show_update),
    url(r'^users/(?P<user_id>\d+)/edit$', views.edit),
    url(r'^users/(?P<user_id>\d+)/destroy$', views.delete),
]

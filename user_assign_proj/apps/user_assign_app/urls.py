from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^userinfo$', views.userinfo),
    url(r'^process$', views.process)
]

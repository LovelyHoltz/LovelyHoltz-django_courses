from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login_register$',views.login_register),
    url(r'^login$',views.login)
]

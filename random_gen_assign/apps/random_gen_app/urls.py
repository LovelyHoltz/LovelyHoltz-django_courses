from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^random_gen_word$', views.random_gen_word),
    url(r'^resetword$', views.resetword)
]

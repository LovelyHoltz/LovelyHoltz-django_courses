from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^programinfo$', views.programinfo),
    url(r'^process$', views.process),
    url(r'^show_me_stacks$', views.stacks)
]

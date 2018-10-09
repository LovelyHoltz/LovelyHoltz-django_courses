from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^myproj$', views.myproj),
    url(r'^aboutme$', views.aboutme),
    url(r'^testimonials$',views.testimonials)
]

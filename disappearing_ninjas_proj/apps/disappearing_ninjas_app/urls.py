from django.conf.urls import url

from . import views

urlpatterns =[
    url(r'^$', views.index),
    url(r'^allninjas/$', views.allninjas),
    url(r'^(?P<ninja>\w+)/$', views.show, name='show')
]

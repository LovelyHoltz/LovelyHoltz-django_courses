from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index),
    url(r'^newninja$',views.newninja),
    url(r'^create$',views.create),
    url(r'^books$',views.books)
]

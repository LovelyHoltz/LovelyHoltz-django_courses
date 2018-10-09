from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^dashboard$', views.dashboard),
    url(r'^logout$', views.logout),
    url(r'^books/add$', views.add),
    url(r'^books/create$', views.create),
    url(r'^books/(?P<book_id>\d+)$', views.show),
    url(r'^reviews/create(?P<book_id>\d+)$', views.create_reviews),
    url(r'^reviews/delete(?P<review_id>\d+)$', views.delete_reviews),
]

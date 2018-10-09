from __future__ import unicode_literals
from django.db import models
from django.contrib import messages

def some_silly_function():
    pass


class UserManager(models.Manager):
    def check_it_out(self, post_data):
        # names must nit be empty
        if len(post_data['first_name'])< 1 or len(post_data['last_name']) < 1 or len(post_data['username']) < 1:
            messages.error("names must not be empty")
        # username must be unique
        # no empty spaces
        print post_data

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    username = models.CharField(max_length = 255, unique=True)
    objects = UserManager()

from __future__ import unicode_literals

from django.db import models
from django.contrib import messages

class UserManager(models.Manager):
    def check_it_out(self, request):
        data_to_check = request.POST

        cool = True
        print data_to_check
        # names must not be empty
        if len(data_to_check['first_name']) < 1 or len(data_to_check['last_name']) < 1 or len(data_to_check['username']) < 1:
            messages.error(request,"name must not be empty")

            cool = False

        if len(data_to_check['first_name']) < MIN_LENGTH or len(data_to_check['last_name']) < MIN_LENGTH:
            messages.error(request, "first/last names must be greater than {}").format(MIN_LENGTH)
            cool = False
        # usernames must be unique
        if self.filter(username=data_to_check['username']) > 0:
            messages.error(request, "username must be unique")
            cool= False
        # no empty spaces

        if cool:
            self.create(
                first_name = data_to_check['first_name'],
                last_name = data_to_check['last_name'],
                username = data_to_check['username']
            )
        return cool

class User(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    username = models.CharField(max_length = 30, unique=True)
    objects = UserManager()

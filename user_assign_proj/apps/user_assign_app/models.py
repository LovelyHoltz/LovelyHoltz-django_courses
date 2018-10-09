from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    firstname = models.CharField(max_length = 255)
    lastname = models.CharField(max_length= 255)
    emailaddress = models.CharField(max_length = 255)
    age = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "First Name: {}, Last Name: {}, Email Address: {}, Age: {}".format(self.firstname, self.lastname, self.emailaddress, self.age)

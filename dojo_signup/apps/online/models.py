from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    robot = models.BooleanField(default=False)

    def __str__(self):
        return "Name: {}, Email: {}, Robot? {}".format(self.name, self.email, self.robot)

    def say_hello(self):
        return "Hi My Name is {}".format(self.name)

class Stack(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    users = models.ManyToManyField(User)

    def __str__(self):
        return "title: {}, description: {}".format(self.title, self.description)

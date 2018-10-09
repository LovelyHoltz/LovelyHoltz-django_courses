from __future__ import unicode_literals

from django.db import models

class Ninja(models.Model):
    dojo = models.CharField(max_length = 100)
    firstname = models.CharField(max_length = 255)
    lastname = models.CharField(max_length = 255)

    def __str__(self):
        return "{} {}".format(self.dojo, self.firstname, self.lastname)

class Book(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField(max_length = 1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    ninja = models.ForeignKey(Ninja, related_name = "books")

    def __str__(self):
        return "{} {}".format(self.name, self.description)


class Author(models.Model):
    firstname = models.CharField(max_length = 255)
    lastname = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    ninja = models.ManyToManyField(Ninja, related_name ="authors")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


    def __str__(self):
        return "{} {}".format(self.firstname, self.lastname, self.email)

from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
    def validateUser(self, post_data):
        errors = []
        if len(post_data["email"]) == 0:
            errors.append("email should not be blank")

        if post_data["password"] == "":
            errors.append("password should not be blank")

        if not post_data["password"] == post_data["confirm_password"]:
            errors.append("password should match the confirm password")

        if len(errors) == 0:
            return True,
        else:
            return False, errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name="wrote_book")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class Review(models.Model):
    book = models.ForeignKey(Book, related_name="reviews")
    user = models.ForeignKey(User, related_name="reviews")
    revcomment = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

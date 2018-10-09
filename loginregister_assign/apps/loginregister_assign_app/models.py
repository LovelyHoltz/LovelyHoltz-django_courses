from __future__ import unicode_literals
import bcrypt, re
from django.db import models
EMAILREG = re.compile(r'^[a-zA-Z0-9.-_+]+@[a-zA-Z0-9.-_]+\.[a-zA-Z]*$')


class UserManager(models.Manager):
    def registration(self, post_data):
        errors = []
        if len(post_data['firstname']) < 2:
            errors.append("first name must be 2 or more characters")
        if len(post_data['lastname']) < 2:
            errors.append("last name must be 2 or more characters")
        if not re.match(EMAILREG,post_data['email']):
            errors.append("email must not be blank")
        if len(post_data['password']) < 8:
            errors.append("password must not be blank")
        if not post_data['password'] == post_data['confirmpassword']:
            errors.append("password must be the same as confirm password")
        if errors:
            return[False, errors]

    def check_login(self, post_data):
        current_user=User.objects.filter(email=post_data['email'])
        if current_user:
            errors.append(['current_user',"Unable to register, please use alternate information"])
            return[False, errors]
        newUser = User(firstname=post_data['firstname'], lastname=post_data['lastname'], email=post_data['email'])
        hashed = bcrypt.hashpw(post_data['password'].encode(), bcrypt.gensalt())
        print hashed,"hashed password"
        newUser.hashpw = hashed
        newUser.save()
        return[newUser]


class User(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    hashpw = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = UserManager()

    def __str__(self):
        return '{} {} {}'.format(self.firstname, self.lastname, self.email)

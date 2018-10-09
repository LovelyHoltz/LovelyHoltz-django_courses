from __future__ import unicode_literals
from .models import User

from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request,'signup_app/index.html')

def signup(request):
    if User.objects.check_it_out(request) == False:
        return  redirect('/')
    return HttpResponse("YAY")

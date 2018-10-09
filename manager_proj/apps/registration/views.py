from django.shortcuts import render
from .models import User
from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request,'registration/index.html')

def signup(request):
    User.objects.check_it_out(request, request.POST)
    return redirect('/')

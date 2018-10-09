from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

def index(request):
    return render(request,'loginregister_assign_app/index.html')

def login_register(request):
    print request.POST
    errs = User.objects.registration(request.POST)
    if errs:
        for e in errs:
            messages.error(request, e)
    else:
        newUser=User.objects.check_login(request.POST)
        request.session['id'] = newUser.id
    return render(request,'loginregister_assign_app/index.html')
    
def login(request):
    print request.POST
    return render(request,'loginregister_assign_app/success.html')

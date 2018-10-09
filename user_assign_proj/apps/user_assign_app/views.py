from django.shortcuts import render, redirect

from . models import User

def index(request):
    return render(request,'user_assign_app/index.html')

def userinfo(request):
    users = User.objects.all()
    context = {
        "all_users" : users
    }
    return render(request,'user_assign_app/userassign.html', context)

def process(request):
    print request.POST
    new_user = User.objects.create(
        firstname = request.POST['firstname'],
        lastname = request.POST['lastname'],
        emailaddress = request.POST['emailaddress'],
        age = request.POST['age']
    )
    return redirect('/userinfo')

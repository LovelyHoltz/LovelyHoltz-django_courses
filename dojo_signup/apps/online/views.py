from django.shortcuts import render, redirect
from .models import User, Stack
# Create your views here.
def index(request):
    return render(request, 'online/index.html')

def programinfo(request):
    users = User.objects.all()
    stacks = Stack.objects.all()
    context = {
        'all_users': users,
        'all_stacks': stacks
    }
    return render(request, 'online/online.html', context)

def process(request):
    print request.POST
    try:
        request.POST['robot']
        robot = True
    except:
        robot = False

    new_user = User.objects.create(
        name = request.POST['name'],
        email = request.POST['email'],
        robot = robot,
    )
    stack_id = request.POST['stack_id']
    Stack.objects.get(id=stack_id).users.add(new_user)

    return redirect('/show_me_stacks')

def stacks():
    stacks = Stack.objects.all()
    context = {
        'all_stacks': stacks
    }
    return render(request,'online/stacks.html', context)

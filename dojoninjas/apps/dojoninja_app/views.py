from django.shortcuts import render, redirect
from . models import Ninja, Book, Author

def index(request):
    return render(request,'dojoninja_app/index.html')

def newninja(request):
    context = {
        'ninjas': Ninja.objects.all()
    }
    return render(request,'dojoninja_app/newninja.html', context)

def create(request):
    Ninja.objects.create(
        dojo = request.POST['dojo'],
        firstname = request.POST['firstname'],
        lastname = request.POST['lastname']
    )
    return redirect('/newninja')

def books(request):
    Book.objects.create(
        name = request.POST['name'],
        description = request.POST['description']
    )
def authors(request):
    Author.objects.create(
        firstname = request.POST['firstname'],
        lastname = request.POST['lastname'],
        email = request.POST['email'],
    )

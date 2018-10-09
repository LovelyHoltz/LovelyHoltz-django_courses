from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'disappearing_ninjas_app/index.html')

def allninjas(request):
    return HttpResponse('<img src="../static/disappearing_ninja_app/img/ninjaimg/donatello.jpg">,<img src="../static/disappearing_ninja_app/img/ninjaimg/leonardo.jpg">,<img src="../static/disappearing_ninja_app/img/ninjaimg/michelangelo.jpg">,<img src="../static/disappearing_ninja_app/img/ninjaimg/raphael.jpg">')

def show(request, ninja):
    if(ninja == "blue"):
        return HttpResponse('<img src="../static/disappearing_ninja_app/img/ninjaimg/leonardo.jpg">')
    elif(ninja=="orange"):
        return HttpResponse('<img src="../static/disappearing_ninja_app/img/ninjaimg/michelangelo.jpg">')
    elif(ninja == "red"):
        return HttpResponse('<img src="../static/disappearing_ninja_app/img/ninjaimg/raphael.jpg">')
    elif(ninja == "purple"):
        return HttpResponse('<img src="../static/disappearing_ninja_app/img/ninjaimg/donatello.jpg">')
    else:
        return HttpResponse('<img src="../static/disappearing_ninja_app/img/ninjaimg/notapril.jpg">')

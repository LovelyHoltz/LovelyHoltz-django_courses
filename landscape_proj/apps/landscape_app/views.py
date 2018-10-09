from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return render(request,'landscape_app/index.html')

def random_routing(request, num):
    num = int(num)
    landscape = ''
    if (num < 10):
        return HttpResponse('<img src="../static/landscape_app/img/landscapes/snow.jpg">')
    elif (num < 20):
        return HttpResponse('<img src="../static/landscape_app/img/landscapes/desert.jpg">')
    elif (num < 30):
        return HttpResponse('<img src="../static/landscape_app/img/landscapes/forest.jpeg">')
    elif (num < 40):
        return HttpResponse('<img src="../static/landscape_app/img/landscapes/vineyard.jpeg">')
    elif (num < 50):
        return HttpResponse('<img src="../static/landscape_app/img/landscapes/tropical.jpg">')
    else:
        return redirect('/')
    context = {
    'landscape': landscape
    }
    return render(request, 'landscape_app/random_routing.html')

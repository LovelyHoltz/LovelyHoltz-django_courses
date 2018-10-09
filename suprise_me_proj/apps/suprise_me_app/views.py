from django.shortcuts import render, HttpResponse
import random
VALUES = ['Monkey', 'Tiger', 'Panda', 'Snake', 'Crocodile', 'Shark' , 'Dog', 'Spider' , 'Dolphin', 'Goat']

def index(request):
    context = {}
    return render(request, 'suprise_me_app/index.html')

def suprise(request):
    random.shuffle(VALUES)
    suprises = []
    for n in range(int(request.POST['number'])):
        suprises.append(VALUES[n])
    context = {'suprises' : suprises}
    print context
    return render(request, 'suprise_me_app/suprise.html', context)
    print 'abcdef'

from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request,'Myportfolio_app/index.html')

def myproj(request):
    return render(request, 'Myportfolio_app/myproj.html')

def aboutme(request):
    return render(request, 'Myportfolio_app/aboutme.html')

def testimonials(request):
    return render(request, 'Myportfolio_app/testimonials.html')

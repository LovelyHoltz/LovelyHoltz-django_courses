from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
    'data': 1234,
    }
    return render(request, 'hello_app/index.html', context)

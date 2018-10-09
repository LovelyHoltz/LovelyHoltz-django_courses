from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
    'data' : 1234
    }
    return render(request,'portfolio_app/index.html', context)
def show(request):
    print request.method
    return render(request,'portfolio_app/testimonials.html')

from django.shortcuts import render
from .models import Products

def index(request):
    Products.objects.create(product_name, description, product_weight,product_category, product_cost)
    products = Products.object.all()
    print products
    return render(request,'products_app/index.html')

def process_products(request):
    if request.POST:
        print request.POST
    return redirect('/')

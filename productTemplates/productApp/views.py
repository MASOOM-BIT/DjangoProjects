from django.shortcuts import render

# Create your views here.
def electronics(request):
    product_dict={
        'product1':'Laptop',
        'product2':'Mobile',
        'product3':'Tablet',
    }

    return render(request, 'productApp/products.html',product_dict)

def toys(request):
    product_dict={
        'product1':'Teddy Bear',
        'product2':'Car',
        'product3':'Doll',
    }

    return render(request, 'productApp/products.html',product_dict)

def shoes(request):
    product_dict={
        'product1':'Nike',
        'product2':'Jordan',
        'product3':'Addidas',
    }

    return render(request, 'productApp/products.html',product_dict)

def index(request):
    return render(request, 'productApp/index.html')
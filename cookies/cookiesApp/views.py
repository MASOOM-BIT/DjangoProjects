from django.shortcuts import render
from django.http import HttpResponse
from .forms import ItemForm
# Create your views here.
def index(request):
    request.session.set_test_cookie()
    return HttpResponse("<h1>Hello, world. You're at the cookies index.</h1>")


def page2(request):
    if request.session.test_cookie_worked():
        print("Test cookie worked!")
        request.session.delete_test_cookie() # delete the test cookie
    else:
        print("Test cookie failed!")
    return HttpResponse("<h1>Hello, world. You're at the cookies page2.</h1>")

def countView(request):
    if 'count' in request.COOKIES:
        count = int(request.COOKIES['count']) + 1
    else:
        count = 1
    response = render(request, 'cookiesApp/count.html', {'count': count})
    # 
    response.set_cookie('count', count)
    return response

def indexView(request):
    return render(request, 'cookiesApp/indexView.html')
def addItem(request):
    form = ItemForm()
    response = render(request, 'cookiesApp/addItem.html', {'form': form})
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item_name = form.cleaned_data['name']
            item_quantity = form.cleaned_data['quantity']
            response.set_cookie(item_name, item_quantity,120)
    return response
    

def displayView(request):
    return render(request, 'cookiesApp/displayView.html', {'cookies': request.COOKIES})



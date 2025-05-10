from django.shortcuts import render
from .forms import ItemForm
# Create your views here.
def pageCount(request):
    count = request.session.get('count', 0)
    count=count+1
    request.session['count'] = count
    return render(request, 'sessionApp/count.html',{'count': count})

def indexView(request):
    return render(request, 'sessionApp/indexView.html')
def addItem(request):
    form = ItemForm()
    response = render(request, 'sessionApp/addItem.html', {'form': form})
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item_name = form.cleaned_data['name']
            item_quantity = form.cleaned_data['quantity']
            response.set_cookie(item_name, item_quantity,120)
    return response
    

def displayView(request):
    return render(request, 'sessionApp/displayView.html', {'cookies': request.COOKIES})

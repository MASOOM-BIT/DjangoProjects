#File Creted by me
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    
    return render(request, 'index.html')

def removepunc(request):
    #Get the text from the user and analyze it
    djtext=(request.GET.get('text', 'default'))
    print(djtext)
    return HttpResponse("<h3>Remove punchuation.</h3>")

def capitalizefirst(request):
    return HttpResponse("<h3>capitalizefirst.</h3>")

def newlineremove(request):
    return HttpResponse("<h3>newlineremove.</h3>")

def spaceremove(request):
    return HttpResponse("<h3>spaceremove.</h3>")

def charcount(request):
    return HttpResponse("<h3>charcount.</h3>")
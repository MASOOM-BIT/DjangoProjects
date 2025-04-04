from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def display(request):
    return HttpResponse("<h1>First App !!</h1>")

def displayDateTime(request):
    dt=datetime.datetime.now()
    s="<h1><b>Current Date and Time: </b></h1>"+str(dt)
    return HttpResponse(s)
#File Creted by me
from django.http import HttpResponse
def index(request):
    return HttpResponse("<h1>Hello, world. You're at the mysite index.</h1>") # Return a string as an HTTP response

def about(request):
    return HttpResponse("Hello,You're at about page of mysite.") # Return a string as an HTTP response

def tutorial_video(request):
    return HttpResponse('''<a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7">Tutorial video source</a>''') # Return a string as an HTTP response
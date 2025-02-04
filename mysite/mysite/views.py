#File Creted by me
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    
    return render(request, 'index.html')

def Analyize(request):
    # Get the text
    djtext = request.GET.get('text', 'default')
    removepunc=request.GET.get('removepunc','off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'Analyize.html', params)

    else:
        return HttpResponse('Error')
    # #Get the text from the user and analyze it
    # djtext = request.GET.get('text', 'default')
    # analyzed=djtext
    # params = {'purpose': "Removing Punctuations", 'analyzed_text': analyzed}
    # return render(request,'Analyize.html',params)
    # # djtext=(request.GET.get('text', 'default'))
    # removepunc=(request.GET.get('removepunc', 'off'))
    # print(removepunc)
    # print(djtext)
    # return HttpResponse("<h3>Remove punchuation.</h3>")

# def capitalizefirst(request):
#     return HttpResponse("<h3>capitalizefirst.</h3>")

# def newlineremove(request):
#     return HttpResponse("<h3>newlineremove.</h3>")

# def spaceremove(request):
#     return HttpResponse("<h3>spaceremove.</h3>")

# def charcount(request):
#     return HttpResponse("<h3>charcount.</h3>")
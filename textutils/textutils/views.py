# I have credated this file....

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html',)
    # return HttpResponse('''<h1>Dipesh Jaiswal</h1> <a href="https://www.facebook.com/"> Django Dipesh Jaiswal FB</a> ''')

def about(request):
    return HttpResponse("About DJ"),

def removepunc(request):
    # Get the text
    djtext = request.GET.get('text', 'default')

    # Analyze the text
    return HttpResponse("remove puns")

def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("new line remove")

def spaceremove(request):
    return HttpResponse("spaceremove <a href='/'> back</a>")

def charcount(request):
    return HttpResponse("charcount")


# Video #10
def analyze(request):
    #Get the text
    djtext= request.POST.get('text', 'default')

    #Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')

    #Check which check-box is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': "Removed Punctuations", 'analyzed_text': analyzed}
        djtext = analyzed


    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Change to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed


    if(newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if(removepunc != 'on' and fullcaps !='on' and newlineremover != 'on'):
        return HttpResponse("Please select at least one operation")

    return render(request, 'analyze.html', params)





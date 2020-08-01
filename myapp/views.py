from django.http import HttpResponse
from django.shortcuts import render

# Create your views herejkhnujvbuj.
def index(request):
    return render(request, 'index.html' )

def next(request):

    taketext= request.POST.get('text', 'default')
    textremove = request.POST.get('textremove', 'off')
    remspace = request.POST.get('remspace', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    lineremove = request.POST.get('lineremove', 'off')
    charcount = request.POST.get('charcount', 'off')


    if textremove == "on":
        ignor = 'vugsacfd'
        mytext = ''

        for char in taketext:
            if char not in ignor:
                mytext = mytext + char
        params = {'message': 'the sentence after editing is ', 'answer': mytext}
        taketext = mytext


    if(lineremove == "on"):
        ignor="\n"
        mytext = ''

        for char in taketext:
            if char not in ignor:
                mytext = mytext + char
        params = {'message': 'The Desired Sentence is', 'answer': mytext}
        taketext = mytext


    if (uppercase == "on"):
        mytext = ''
        for char in taketext:
            mytext = mytext + char.upper()
        params = {'message': 'The Desired Sentence is', 'answer': mytext}
        taketext = mytext


    if (remspace == "on"):
        mytext = ''
        for index,char in enumerate(taketext):
            if not(taketext[index] == ' ' and taketext[index+1] == ' '):
                mytext = mytext + char
        params = {'message': 'The Desired Sentence is', 'answer': mytext}


    if uppercase == "off" and remspace == "off" and lineremove == "off" and textremove == "off":
        return HttpResponse("error")


    return render(request, 'next.html', params)




#I have created this file
from django.http import HttpResponse
from django.shortcuts import render

#def index(request):
#    return HttpResponse('''<h1>Hello</h1> <a href ="https://www.facebook.com/"> Facebook</a>''')
#def about(request):
#    return HttpResponse('sagar')

def index(request):
    return render(request,'index.html')

def analyze(request):
    #Get the text
    djtext = (request.GET.get('text','default'))
    #check box value
    removepunc = (request.GET.get('remove', 'off'))
    fullcase = (request.GET.get('fullcase', 'off'))
    newline =(request.GET.get('newline','off'))
    if removepunc == "on":
        punctuation = '''!(-[]{};:"./@$^&_-'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char

        params = {'purpose': 'Remove punctuation', 'analysed_text': analyzed}
        # analyze the text
        return render(request, 'Analyse.html', params)
    elif (fullcase == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'changed_upper case', 'analysed_text': analyzed}
            # analyze the text
        return render(request, 'Analyse.html', params)
    elif (newline=='on'):
        analyzed = ""
        for char in djtext:
            if char !="\n":
                analyzed = analyzed + char
        params = {'purpose': 'NEWLINE punctuation', 'analysed_text': analyzed}
        # analyze the text
        return render(request, 'Analyse.html', params)
    elif (extraspace=='on'):
        analyzed = ""
        for index,char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                analyzed = analyzed + char
        params = {'purpose': 'extraspace punctuation', 'analysed_text': analyzed}
        # analyze the text
        return render(request, 'Analyse.html', params)
    else:
        return HttpResponse('error')








def navi(request):
    s='''<h2>Navigator Bar <br></h2>
    <li><a href="https://www.codewithharry.com/videos/
    python-django-tutorials-hindi-10>Django with sagar</a></br></li>
    <li><a href = "https://www.facebook.com/">Facebook Sagar</a></br></li>
    <li><a href = "https://www.flipkart.com/">flipkart sagar</a></br></li>'''
    return HttpResponse(s)



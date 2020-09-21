from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'main_page.html')

def analyze(request):
    entered_text = request.GET.get('text','default')
    uppercase = request.GET.get('UPPERCASE','off')
    lowercase = request.GET.get('lowercase','off')
    removepunc = request.GET.get('removepunc','off')
    charcount = request.GET.get('charcount','off')
    analyzed = ""
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in entered_text:
            if char not in punctuations:
                analyzed = analyzed + char
        text_dict= {'edited_text': analyzed}
        return render(request, 'analyze.html', text_dict)
    elif uppercase == "on":
        analyzed = entered_text.upper()
        text_dict = {'edited_text': analyzed}
        return render(request, 'analyze.html', text_dict)
    elif lowercase == "on":
        analyzed = entered_text.lower()
        text_dict = {'edited_text': analyzed}
        return render(request, 'analyze.html', text_dict)
    elif charcount == "on":
        c = len(entered_text)
        text_dict = {'edited_text': f"Length is {c}"}
        return render(request, 'analyze.html', text_dict)
    else:
        return HttpResponse("Please select one option!!!")



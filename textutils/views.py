# I have created this file
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def analyzer(request):
    txt=request.POST.get('text','off')
    chck_analyzer=request.POST.get('check_analyzer','off')
    fullcaps=request.POST.get('capitalyze','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremove=request.POST.get('extraspaceremover','off')
    totalcharacters=request.POST.get('charcount','off')
    analyzed=""
    punctuations='''!()-{}[];:'"\,<>./?@#$%^&*_~'''
    if chck_analyzer=='on' and fullcaps=='on' and extraspaceremove=='on':
        analyzed = ""
        for index,char in enumerate(txt):
            if char not in punctuations and not (txt[index]==" " and txt[index+1]==" "):
                analyzed += char
        analyzed = analyzed.upper()
        params = {'purpose': 'after removing punctuations, capitalyzing and extra spaces', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif chck_analyzer=='on' and fullcaps=='on':
        analyzed = ""
        for char in txt:
            if char not in punctuations:
                analyzed += char
        analyzed=analyzed.upper()
        params = {'purpose': 'after removing punctuations and capitalyzing', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif chck_analyzer=="on":
        for char in txt:
            if char not in punctuations:
                analyzed+=char
        params={'purpose':'Remove punctuations','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    elif fullcaps=='on':
        analyzed=""
        for char in txt:
            analyzed+=char.upper()
        params = {'purpose': 'changes to uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif newlineremover=='on':
        analyzed=""
        for char in txt:
            if char!="\n" and char!="\r":
                analyzed+=char
        params = {'purpose': 'remove of newline', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif extraspaceremove=='on':
        analyzed=""
        for index,char in enumerate(txt):
            if not (txt[index]==" " and txt[index+1]==" "):
                analyzed+=char
        params = {'purpose': 'remove of extra spaces', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif totalcharacters=='on':
        count=0
        for char in txt:
            if (char>='a' and char<='z') or (char>='A' and char<='Z'):
                count+=1
        params = {'purpose': 'total characters ', 'analyzed_text': count}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")
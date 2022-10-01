# I have created this file myself.
from django.http import HttpResponse
from django.shortcuts import render


def index(req):
    params = {'page': 1}

    return render(req, 'index.html', params)


def about(req):
    params = {'page': 2}
    return render(req, 'about.html', params)


def contact(req):
    params = {'page': 3}
    return render(req, 'contact.html', params)


def analyze(req):
    # Getting Text
    txt = req.POST.get('text', 'default')

    # Checking Switches
    removePunc = req.POST.get('removePunc', 'off')
    fullCap = req.POST.get('fullCap', 'off')
    newlineRemover = req.POST.get('newlineRemover', 'off')
    extraSpaceRemover = req.POST.get('extraSpaceRemover', 'off')
    charCounter = req.POST.get('charCounter', 'off')

    # Applying
    if removePunc == 'on':
        analyzedTxt = ''
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in txt:
            if char not in punc:
                analyzedTxt += char
        txt = analyzedTxt

    if fullCap == 'on':
        analyzedTxt = txt.upper()
        txt = analyzedTxt

    if newlineRemover == 'on':
        analyzedTxt = ''
        for char in txt:
            if char != '\n' and char != '\r':
                analyzedTxt += char
        txt = analyzedTxt

    if extraSpaceRemover == 'on':
        analyzedTxt = ''
        for index, char in enumerate(txt):
            if not(char == ' ' and txt[index+1] == ' '):
                analyzedTxt += char
        txt = analyzedTxt

    if charCounter == 'on':
        analyzedTxt = f'Total lenght of characters are : {len(txt)}'
        txt = txt + '\n' + analyzedTxt

    if removePunc != 'on' and fullCap != 'on' and newlineRemover != 'on' and extraSpaceRemover != 'on' and charCounter != 'on':
        return render(req, '404.html')

    params = {
        'analyzedTxt': txt,
        'page': 1,
    }

    return render(req, 'analyze.html', params)

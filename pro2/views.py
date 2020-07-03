from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    params = {'name': 'papa', 'sher': 'gao'}
    return render(request, 'index.html', params)
    # HttpResponse('<button>hey</button>')


def second(request):
    return HttpResponse('<a href="/">hey</button>')


def npage(request):
    djtext = request.POST.get('text', 'default')
    analyse = ""
    punctuation = "!@#$%^&*?><:"
    ck = request.POST.get('punct', 'off')
    print(ck)
    cap = request.POST.get('caps', 'off')
    spc = request.POST.get('spaceremove', 'off')
    chrc = request.POST.get('charcount', 'off')
    print(ck)
    if ck == "on":
        for char in djtext:
            if char not in punctuation:
                analyse = analyse + char
        params = {'pucn': 'searching..', 'royal': analyse}
        djtext=analyse
        print(djtext)
        #return render(request, 'punctu.html', params)

    if cap == "on":
        for char in djtext:
            if char not in punctuation:
                analyse = analyse + char.upper()
        djtext = analyse
        #return HttpResponse(analyse)

    if spc == "on":
        analyse = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyse = analyse + char
        djtext = analyse
        #return HttpResponse(analyse)

    if chrc == "on":
        count= len(djtext)
        #return HttpResponse(len(djtext))
       # return djtext,count

    return HttpResponse(djtext)


def punctu(request):
    s = '''<a href ='https://practice.geeksforgeeks.org/explore/?category%5B%5D=Arrays&company%5B%5D=Amazon&page=1'>gfg</a> </br>
     <a href ='https://practice.geeksforgeeks.org/explore/?category%5B%5D=Arrays&company%5B%5D=Amazon&page=1'>gfg</a> </br>
     <a href ='https://practice.geeksforgeeks.org/explore/?category%5B%5D=Arrays&company%5B%5D=Amazon&page=1'>gfg</a> </br>
     <a href ='https://practice.geeksforgeeks.org/explore/?category%5B%5D=Arrays&company%5B%5D=Amazon&page=1'>gfg</a> </br>
     <a href ='https://practice.geeksforgeeks.org/explore/?category%5B%5D=Arrays&company%5B%5D=Amazon&page=1'>gfg</a> </br>

     '''

    return HttpResponse(s)


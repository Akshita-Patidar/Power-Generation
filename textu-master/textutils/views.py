# i have created this file--akshita
from django.http import HttpResponse
from django.shortcuts import render


# code for video 6

# def index(request):
#     return HttpResponse('''<h1>hello</h1> <a href="https://www.youtube.com/results?search_query=codewithharry+django"> Django CodewithHarry</a>''')
#
# def about(request):
#     return HttpResponse("hello about")

# code for video 7

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("<h1>Home</h1>")


# def ex1(request):
#     sites=['''<h1>FOR ENTERTAINMENT</h1>
#             <a href="https://www.youtube.com">youtube video</a>'''
#            '''<h1>FOR INTERACTION</h1>
#                <a href="https://www.facebook.com">Facebook</a>'''
#            '''<h1>FOR INSIGHT</h1>
#                <a href="https://www.ted.com/talks">Ted</a>'''
#            '''<h1>FOR INTERNSHIP</h1>
#                <a href="https://internshala.com">Internship</a>'''
#            ]
#     return HttpResponse((sites))

def analyze(request):
    djtext = request.POST.get('text', 'default')
    djtext1 = request.POST.get('text1', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')

    if (removepunc == 'on' and fullcaps == 'on'):
        power = 0.168 * djtext * (djtext1 ** 3)
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': power}

    if (removepunc != "on" and fullcaps != "on"):
        return HttpResponse("Please select the operation")
    return render(request, 'analyze.html', params)

    # analyzed=djtext


    # if (fullcaps == "on"):
    #     analyzed = ""
    #     for char in djtext:
    #         analyzed = analyzed + char.upper()
    #     params = {"purpose": "Changed to Uppercase", "analyzed_text": analyzed}
    #     djtext = analyzed
    #     # return render(request, "analyze.html", params)
    #
    # if (newlineremover == "on"):
    #     analyzed = ""
    #     for char in djtext:
    #         if char != "\n":
    #                 analyzed = analyzed + char
    #     params = {"purpose": "Removed new lines", "analyzed_text": analyzed}
    #     djtext = analyzed
    #     # return render(request, "analyze.html", params)
    #
    # if (extraspaceremover == "on"):
    #     analyzed = ""
    #     for index, char in enumerate(djtext):
    #         if djtext[index] == " " and djtext[index + 1] == " ":
    #             pass
    #         else:
    #             analyzed = analyzed + char.upper()
    #     params = {"purpose": "Changed to Uppercase", "analyzed_text": analyzed}
    #
    #     return render(request, "analyze.html", params)
    # if (removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on"):
    #     return HttpResponse("please select any operation and try again")

    # return render(request, 'analyze.html', params)


# def removepunc(request):
#     #get the text
#     djtext=print(request.GET.get("text","default"))
#     print((djtext))
#     #analyze the text
#     return HttpResponse("remove Punc")
#
# def capfirst(request):
#     return HttpResponse("capitalizefirst")
#
# def newlineremove(request):
#     return HttpResponse("new line remove")
#
# def spaceremove(request):
#     return HttpResponse("space remove <a href='/'> back </a>")
#
# def charcount(request):
#     return HttpResponse("char count")

from django.shortcuts import render

from django.http import HttpResponse


def homePageView(request):
    context = {'dummy_list': []}
    return render(request, 'fly/home.html', context)
    #return HttpResponse("Hello, Fly!")


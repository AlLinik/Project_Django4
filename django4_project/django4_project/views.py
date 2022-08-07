from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    a = 9 + 6
    return render(request, 'about.html', {'tuple': a})


def home(request):
    return HttpResponse('This is home')

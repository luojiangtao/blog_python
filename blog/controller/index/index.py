from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'index/index.html', context)
def detail(request):
    return HttpResponse("1")
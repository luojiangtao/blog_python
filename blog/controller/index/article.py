from django.http import HttpResponse
from django.shortcuts import render

def list(request):
    return render(request, 'index/list.html')
def detail(request):
    return render(request, 'index/detail.html')
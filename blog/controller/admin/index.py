from django.http import HttpResponse

def index(request):
    return HttpResponse("index ! ")
def detail(request):
    return HttpResponse("detail ! ")
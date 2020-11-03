from django.http import HttpResponse


def index(request):
    return HttpResponse('index page is here')

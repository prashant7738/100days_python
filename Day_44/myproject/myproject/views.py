from django.http import HttpResponse


def home_page(request):
    return HttpResponse("Hello world")


def about(request):
    return HttpResponse("This is my about page")
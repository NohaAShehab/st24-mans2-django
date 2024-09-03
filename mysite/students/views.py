from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# def view function --> handle http request
def hello(request):
    print(request)
    return HttpResponse("Hello world from iti")
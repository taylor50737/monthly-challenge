from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def january(request):
    return HttpResponse("This works!")

def february(request):
    return HttpResponse("Walk for at least 20 minutes every day!")
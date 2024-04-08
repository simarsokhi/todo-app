from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def view1(response):
    return HttpResponse("<h1>hi</h1>")

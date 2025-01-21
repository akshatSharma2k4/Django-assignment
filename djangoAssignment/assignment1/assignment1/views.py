from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

def home(req):
    return render(req, 'assignment1/home.html')

def about(req):
    return HttpResponse("<h1>This is a About page<h1>")

def contact(req):
    return HttpResponse("<h1>This is a Contact page<h1>")

def custom404(req):
    return render(req, 'assignment1/404.html')

from django.shortcuts import render, redirect, HttpResponse
# CONTROLLER!!!
# Create your views here.

def index(request):
    response = "Hello, I am your first request!"
    return HttpResponse(response)

def index(request):
    # print ("6"*4)
    return render(request, "first_django_app/index.html")

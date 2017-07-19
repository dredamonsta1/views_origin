from django.shortcuts import render, HttpResponse
# ******************CONTROLLER***********************
# Create your views here.
def index(request):
    response = "hey just checking if its working"
    return render(request, "first_app/index.html")

def accounts(request):
    return render(request,"first_app/account_home.html")

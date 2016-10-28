from django.shortcuts import render

# Create your views here.
def index(request):
    response = "your welcome"
    return render(request,"views_app/index.html")

def login(request):
    print(request.method)
    return render(request, 'views_app/login.html')

def reg(request):
    print(request.method)
    return render(request, 'views_app/reg.html')

def users(request):
    print(request.method)
    return render(request, 'views_app/users.html')






    return redirect('/')

from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "email": "imamonsta1@aim.com",
        "name": "andre"
    }
    return render(request,"first_app/index.html", context)

def show(request, id):
    context = {
        "id": id
    }
    return render(request,"first_app/show.html", context)

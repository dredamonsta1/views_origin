from django.shortcuts import render
from .models import People
# Create your views here.
def index(request):
    People.objects.create(first_name="Andre", last_name="Wilkinson")
    people = People.objects.all()
    print (people)

    return render(request,"the_wall_app/index.html")

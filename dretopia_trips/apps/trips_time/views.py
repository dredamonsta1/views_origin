from django.shortcuts import render, redirect

from django.contrib import messages
# from .models import User

# Create your views here.
def index(request):
    return render(request, 'trips_time/index.html')


def add_plan(request):
    return render(request, 'trips_time/dashboard')
    pass



def login(request):
    if request.method == "POST":
        User.objects.login(request.POST)
        if not user:
            messages.error(request, "Invalid login dude")
        else:
            request.session['logged_user'] = user.id
            messages.success(request, "your good {}!".format(user.first_name))
            return redirect('/travle_dashboard')


    return redirect('/')





# return redirect('/')

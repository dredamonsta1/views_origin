from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'log_reg/index.html')

def success(request):
    return render(request, 'log_reg/success.html')


def login(request):
    if request.method == "POST":
        User.objects.login(request.POST)
        if not user:
            messages.error(request, "Invalid login dude")
        else:
            request.session['logged_user'] = user.id
            messages.success(request, "your good {}!".format(user.first_name))
            return redirect('/success')


    return redirect('/')
    #  return HttpResponse("login view")
    # result = User.objects.validateLogin(request)

    # if result[0] == False:
        # print_messages(request, result[1])
        # return redirect(reverse('index'))

    # return log_user_in(request, result[1])

def register(request):
    if request.method == "POST":

        form_errors = User.objects.validate_user_info(request.POST)

    if len(form_errors) > 0:
        for error in form_errors:
            messages.error(request,error)
        else:
            user = User.objects.register(request.POST)
            messages.success(request, "your good b")


    return redirect('/')

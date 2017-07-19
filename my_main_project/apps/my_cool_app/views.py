from django.shortcuts import render

# Create your views here.
def index(request):

    context = {
        "my_cool_variable": "wanda",
        "major": "key"
    }

    return render(request,'my_cool_app/index.html', context)

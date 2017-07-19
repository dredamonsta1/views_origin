from django.shortcuts import render

# Create your views here.

def index(request):

    context = {
        "codeing_doge": ""
    }
    return render(request, 'codeing_doge/index.html', context)

]

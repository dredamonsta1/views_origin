from django.shortcuts import render, HttpResponse, redirect

# import request
# Create your views here.
def index(request):return render(request, 'survey_form_app/index.html')
pass

def runThis():
    return redirect('/')

from django.conf.urls import url, include
from . import views

# models -- views --TEMPLATES

def index(request):
    print ("dipset")
urlpatterns = [
    url(r'^$', views.index)
]

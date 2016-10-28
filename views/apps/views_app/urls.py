from django.conf.urls import url
from . import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^reg$', views.reg),
    url(r'^users$', views.users),
]

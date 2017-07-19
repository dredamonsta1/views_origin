from django.conf.urls import url
from . import views
urlpatterns = [

    url(r'^$', views.index),
    url(r'^login$', views.index),
    url(r'^add_plan$', views.add_plan),
    # url(r'^success$', views.success),

]

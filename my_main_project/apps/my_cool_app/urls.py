from django.conf.urls import url
from . import views
# def index(request):
#     return "hi"

urlpatterns = [
    url(r'^$', views.index)
    # url(r'^admin/', admin.site.urls),
]

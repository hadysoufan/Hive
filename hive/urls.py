from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def getHome(request):
    return HttpResponse("Hello, world. You're at the home page.")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', getHome, name='home')
   
]

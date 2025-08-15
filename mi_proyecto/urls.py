
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

def inicio(request):
    return HttpResponse("<h1>Bienvenido a mi página de Custom Shoes 👟</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
]

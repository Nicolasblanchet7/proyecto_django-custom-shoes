from django.urls import path
from . import views

urlpatterns = [
    path('', views.presentacion, name='presentacion'),
]

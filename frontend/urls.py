from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("weight/", views.weight, name="weight"),
    path("temperature/", views.temperature, name="temperature"),
]

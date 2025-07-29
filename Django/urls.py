from django.contrib import admin
from django.urls import path
import hitapp.views

urlpatterns = [
    path("",hitapp.views.home),
    path("pred/",hitapp.views.pred)
]

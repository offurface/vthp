from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),


]

from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),

    path('file/', include([
        #path('', views.FileListView.as_view(), name='sport-type-list'),

    ])),

    path('student/', include([
        #path('', views.StudentListView.as_view(), name='sport-type-list'),

    ])),

]

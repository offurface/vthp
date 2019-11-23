from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import (
    Student,
    File,
)
from django.views.generic import (
    View,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)

class MainView(View):

    def get(self, request, *args, **kwargs):

        files = File.objects.all()

        return render(request, "main/main.html", {
            "files": files,
        })

    def post(self, request, *args, **kwargs):


        return render(request, "main/main.html")

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
from .forms import UploadFileForm

class MainView(View):

    def get(self, request, *args, **kwargs):

        form = UploadFileForm

        return render(request, "main/main.html", {
            "form": form,
        })

    def post(self, request, *args, **kwargs):


        return render(request, "main/main.html")

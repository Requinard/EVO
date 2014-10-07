from django.shortcuts import render
from django.views.generic import View
from .forms import LoginForm, ExampleForm

# Create your views here.
class IndexView(View):
    def get(self, request):
        return render(request, "test.html", {"example_form": LoginForm()})
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import LoginForm, ExampleForm

# Create your views here.
class IndexView(View):
    def get(self, request):
        return render(request, "test.html", {"example_form": LoginForm()})

class LoginView(View):
    def get(self, request):
        return redirect("public:index")
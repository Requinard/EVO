from django.shortcuts import render
from django.views.generic import View
from django.http.response import HttpResponse

# Create your views here.
class IndexView(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Hi")
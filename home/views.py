from django.shortcuts import render
from django.views.generic import View

from .models import Post
from .forms import PostForm


# Create your views here.
class IndexView(View):
    def get(self, *args, **kwargs):
        context = {}
        context['posts'] = Post.objects.filter(owner=self.request.user)
        context['create_post_form'] = PostForm()
        return render(self.request, "home/index.html", context)
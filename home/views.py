from django.shortcuts import render
from django.views.generic import View
from django.contrib import messages

from .forms import SelfPostForm
from .models import Post




# Create your views here.
class IndexView(View):
    def get(self, *args, **kwargs):
        context = {}
        context['posts'] = Post.objects.filter(owner=self.request.user)
        context['create_post_form'] = SelfPostForm()
        return render(self.request, "home/index.html", context)

class CreateNewPostView(View):
    def post(self, *args, **kwargs):
        form = SelfPostForm(self.request.POST)

        if form.is_valid():
            post = Post()
            post.owner = self.request.user
            post.post_body = form.cleaned_data['post_body']

            if post.save():
                messages.success(self.request, "Succesfully posted your post.")

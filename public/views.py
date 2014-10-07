from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.views.generic import View
from django.http.response import HttpResponseForbidden
from django.contrib import messages
from .forms import LoginForm


on_successfull_login = "admin:index"

# Create your views here.
class IndexView(View):
    def get(self, request):
        if self.request.user is not None:
            redirect(on_successfull_login)
        return render(request, "public/index.html", {"login_form": LoginForm()})
    def post(self, *args, **kwargs):
        if self.request.user is not None:
            redirect(on_successfull_login)
        return render(self.request, "public/index.html", {"login_form": LoginForm()})

class LoginView(View):
    def get(self, request):
        return redirect("public:index")

    def post(self, *args, **kwargs):
        post = self.request.POST
        form = LoginForm(post or None)

        print form

        if form.is_valid:
            print form.cleaned_data
            try:
                user_model = User.objects.get(email=form.cleaned_data['email'])

                if user_model is None:
                    user_model = User.objects.get(username=form.cleaned_data['email'])
                    # Allow login with username instead of email

                user = authenticate(username=user_model.username, password=form.cleaned_data['password'])
                if user is not None:
                    if user.is_active:
                        login(self.request, user)
                        messages.success(self.request, "You were succesfully logged in.")
                        return redirect(on_successfull_login)
                    else:
                        messages.error(self.request, "Your account is disabled")
                        return redirect("public:index")
                else:
                    messages.error(self.request, "Your email or password was incorrect.")
                    return redirect("public:index")
            except:
                print 'Invalid password'
                messages.error(self.request, "Your email or password was incorrect.")
                return redirect("public:index")
        else:
            print "invalid user"
            messages.warning(self.request, "Your input was not valid.")
            return redirect("public:index")

class LogoutView(View):
    def get(self, *args, **kwargs):
        if logout(self.request):
            messages.success(self.request, "You were succesfully logged out.")
        else:
            messages.error(self.request, "Something went wrong during logging out.")

        return redirect("public:index")

    def post(self, *args, **kwargs):
        if self.request.user is not None:
            if not logout(self.request):
                messages.success(self.request, "You were succesfully logged out.")
            else:
                messages.error(self.request, "Something went wrong during logging out.")

        return redirect("public:index")\

class TestView(View):
    def get(self, *args, **kwargs):
        return render(self.request, "base.html", {})
from django.conf.urls import url, patterns

from views import *

urlpatterns = patterns(
    '',
    url(r'^login/', LoginView.as_view(), name="login"),
    url(r'^logout/', LogoutView.as_view(), name="logout"),
    url(r'^register/', RegisterView.as_view(), name="register"),
    url(r'^test/$', TestView.as_view()),
    url(r'$', IndexView.as_view(), name="index"),
)
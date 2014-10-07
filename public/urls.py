from django.conf.urls import url, patterns

from views import *

urlpatterns = patterns(
    '',
    url(r'^login/', LoginView.as_view(), name="login"),
    url(r'$', IndexView.as_view(), name="index"),
)
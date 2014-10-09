from django.conf.urls import url, patterns

from views import *

urlpatterns = patterns(
    '',
    url(r'post/new/'),
    url(r'^', IndexView.as_view(), name="index"),
)
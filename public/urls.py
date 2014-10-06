from django.conf.urls import url, patterns

from views import *

urlpatters = patterns(
    '',
    url(r'^', IndexView.as_view()),
)
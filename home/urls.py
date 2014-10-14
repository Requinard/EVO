from django.conf.urls import url, patterns

from views import *

urlpatterns = patterns(
    '',
    url(r'post/new/', CreateNewPostView.as_view(), name="create_new_post"),
    url(r'^', IndexView.as_view(), name="index"),
)
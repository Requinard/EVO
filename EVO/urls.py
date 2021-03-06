from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'EVO.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', include('home.urls', namespace="home")),
    url('^activity/', include('actstream.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^', include('public.urls', namespace="public")),
)

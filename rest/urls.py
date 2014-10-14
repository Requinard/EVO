from rest_framework import routers
from django.conf.urls import url, patterns, include
import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = patterns(
    '',
    url(r'^api_auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),

)
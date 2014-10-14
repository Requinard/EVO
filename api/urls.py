from rest_framework import routers
from django.conf.urls import url, patterns, include
import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'user_settings', views.UserSettingsViewSet)

urlpatterns = patterns(
    '',
    url(r'^api_auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),

)
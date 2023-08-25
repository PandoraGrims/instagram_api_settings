from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from api_v1.views import get_csrf_token, ApiViewSet

app_name = "api_v1"

router = DefaultRouter()
router.register("posts", ApiViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("get-csrf-token/", get_csrf_token),
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

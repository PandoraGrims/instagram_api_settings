from django.urls import path

from api_v1.views import get_csrf_token

app_name = "api_v1"

urlpatterns = [
    path("get-csrf-token/", get_csrf_token),
]

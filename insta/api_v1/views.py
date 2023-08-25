from _decimal import Decimal

from django.http import HttpResponse, JsonResponse, FileResponse, HttpResponseNotAllowed
import json
from datetime import datetime
from rest_framework.viewsets import ModelViewSet
from django.views.decorators.csrf import ensure_csrf_cookie

from api_v1.serializers import PostSerializer
from webapp.models import Post


@ensure_csrf_cookie
def get_csrf_token(request, *args, **kwargs):
    if request.method == "GET":
        return HttpResponse()
    return HttpResponseNotAllowed(['GET'])


class ApiViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

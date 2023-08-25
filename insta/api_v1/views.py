from django.http import HttpResponse, HttpResponseNotAllowed
from rest_framework.permissions import IsAuthenticated
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

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

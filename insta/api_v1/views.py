from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from api_v1.serializers import PostSerializer
from webapp.models import Post
from rest_framework.decorators import action


class ApiViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        return Response(PostSerializer(self.get_object()).data)

    def get_serializer_class(self):
        if self.action in ("retrieve", "list"):
            return PostSerializer
        return PostSerializer

    def get_permissions(self):
        super().get_permissions()
        if self.request.method in SAFE_METHODS:
            return []
        return [IsAuthenticated()]

    @action(methods=["GET"], detail=True, url_path="like_users")
    def get_likes_count(self, request, *args, **kwargs):
        post = self.get_object()
        return Response({"like_users": post.like_users.count()})

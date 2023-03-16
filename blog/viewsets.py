from django.shortcuts import render
from rest_framework import viewsets, permissions
# blog app called models are
from .models import BlogModel, BlogCategoryModel, BlogCommentModel, BlogTagModel

# blog app called serializers are
from .serializers import BlogModelSerializer, BlogCategoryModelSerializer, BlogCommentModelSerializer, \
    BlogTagModelSerializer


# BlogViewSet for BlogModelSerializer
class BlogViewSet(viewsets.ModelViewSet):
    queryset = BlogModel.objects.all()
    serializer_class = BlogModelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]


# BlogCategoryViewSet for BlogCategoryModelSerializer
class BlogCategoryViewSet(viewsets.ModelViewSet):
    queryset = BlogCategoryModel.objects.all()
    serializer_class = BlogCategoryModelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]


# BlogCommentViewSet for BlogCommentModelSerializer
class BlogCommentViewSet(viewsets.ModelViewSet):
    serializer_class = BlogCommentModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = BlogCommentModel.objects.filter(user=self.request.user)
        return queryset


# BlogTagViewSet for BlogTagModelSerializer
class BlogTagViewSet(viewsets.ModelViewSet):
    queryset = BlogTagModel.objects.all()
    serializer_class = BlogTagModelSerializer

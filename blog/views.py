from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import BlogModel, BlogCategoryModel, BlogCommentModel, BlogTagModel

from .serializers import BlogModelSerializer, BlogCategoryModelSerializer, BlogCommentModelSerializer, \
    BlogTagModelSerializer


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


class BlogCategoryViewSet(viewsets.ModelViewSet):
    queryset = BlogCategoryModel.objects.all()
    serializer_class = BlogCategoryModelSerializer


class BlogCommentViewSet(viewsets.ModelViewSet):
    serializer_class = BlogCommentModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = BlogCommentModel.objects.filter(user=self.request.user)
        return queryset


class BlogTagViewSet(viewsets.ModelViewSet):
    queryset = BlogTagModel.objects.all()
    serializer_class = BlogTagModelSerializer

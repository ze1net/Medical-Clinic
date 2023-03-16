from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from .models import ServiceCategoryModel, ServiceModel, ServiceCommentModel, ServiceTagModel
from .serializers import ServiceCategorySerializer, ServiceSerializer, ServiceCommentSerializer, ServiceTagSerializer


class ServiceCategoryViewSet(viewsets.ModelViewSet):
    queryset = ServiceCategoryModel.objects.all()
    serializer_class = ServiceCategorySerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = ServiceModel.objects.all()
    serializer_class = ServiceSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]




class ServiceCommentViewSet(viewsets.ModelViewSet):
    queryset = ServiceCommentModel.objects.all()
    serializer_class = ServiceCommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = ServiceCommentModel.objects.filter(user=self.request.user)
        return queryset


class ServiceTagViewSet(viewsets.ModelViewSet):
    queryset = ServiceTagModel.objects.all()
    serializer_class = ServiceTagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

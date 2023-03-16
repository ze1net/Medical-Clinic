from rest_framework import viewsets, permissions

# staff app called models are
from .models import StaffCategoryModel, DirectionModel, EmployeeModel

# staff app called serializers are
from .serializers import StaffCategoryModelSerializer, DirectionModelSerializer, EmployeeModelSerializer

'''All ViewSets created in this file can only be used by admin'''


# StaffCategoryViewSet for StaffCategoryModelSerializer
class StaffCategoryViewSet(viewsets.ModelViewSet):
    queryset = StaffCategoryModel.objects.all()
    serializer_class = StaffCategoryModelSerializer

    # function for permissions
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]


# DirectionViewSet for DirectionModelSerializer
class DirectionViewSet(viewsets.ModelViewSet):
    queryset = DirectionModel.objects.all()
    serializer_class = DirectionModelSerializer

    # function for permissions
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]


# EmployeeViewSet for EmployeeModelSerializer
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeModelSerializer
    permissions = [permissions.IsAuthenticated]

    # function for permissions
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

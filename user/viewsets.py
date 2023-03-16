# Rest Framework viewsets, permissions classes are used
from rest_framework import viewsets, permissions

# from models import user app models are called
from user.models import CountryModel, RegionModel, CityModel

# from serializers import user app serializers are called
from .serializers import CountryModelSerializer, RegionModelSerializer, CityModelSerializer

'''All ViewSets created in this file can only be used by admin'''


# CountryViewSet for CountryModelSerializer
class CountryViewSet(viewsets.ModelViewSet):
    queryset = CountryModel.objects.all()
    serializer_class = CountryModelSerializer

    # function for permissions
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]


# RegionViewSet for RegionModelSerializer
class RegionViewSet(viewsets.ModelViewSet):
    queryset = RegionModel.objects.all()
    serializer_class = RegionModelSerializer

    # function for permissions
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]


# CityViewSet for CityModelSerializer
class CityViewSet(viewsets.ModelViewSet):
    queryset = CityModel.objects.all()
    serializer_class = CityModelSerializer

    # function for permissions
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

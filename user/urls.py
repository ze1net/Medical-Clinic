# path, include for use in urlpatterns extracted from django.urls
from django.urls import path, include
# Rest Framework routers classes are used
from rest_framework import routers

# user app viewsets, views called viewsets, views files
from .viewsets import CityViewSet, RegionViewSet, CountryViewSet
from .views import UserProfileView

# application name user
app_name = 'user'

'''DRF routers classes are used for viewsets'''
# To use routers, a variable named router is created and the SimpleRouter() function is loaded into it
router = routers.SimpleRouter()

# Viewsets are added to routers via register()
router.register('country', CountryViewSet, basename='country')
router.register('region', RegionViewSet, basename='region')
router.register('city', CityViewSet, basename='city')

# created urlpatterns to bind to the main config.urls
urlpatterns = [
    # paths for views
    path('profile/', UserProfileView.as_view(), name='profile'),
    # include routers.urls
    path('profile-data/', include(router.urls)),
]

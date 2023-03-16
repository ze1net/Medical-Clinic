# Called to write path from DRF routers classes
from rest_framework import routers

from .viewsets import StaffCategoryViewSet, DirectionViewSet, EmployeeViewSet

router = routers.SimpleRouter()
router.register('category', StaffCategoryViewSet, basename='staff-category')
router.register('direction', DirectionViewSet, basename='direction')
router.register('employee', EmployeeViewSet, basename='employee')

urlpatterns = router.urls

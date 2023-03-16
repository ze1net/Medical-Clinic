from rest_framework import routers
from .viewsets import ServiceCategoryViewSet, ServiceViewSet, ServiceCommentViewSet, ServiceTagModel, ServiceTagViewSet

router = routers.SimpleRouter()
router.register('s-category', ServiceCategoryViewSet, basename='service-category')
router.register('service', ServiceViewSet, basename='service')
router.register('s-comment', ServiceCommentViewSet, basename='service-comment')
router.register('s-tag', ServiceTagViewSet, basename='service-tag')

urlpatterns = router.urls
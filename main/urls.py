from rest_framework import routers
from .viewsets import ContactUsViewSet, AboutUsViewSet

router = routers.SimpleRouter()
router.register('contact-us', ContactUsViewSet, basename='contact-us')
router.register('about-us', AboutUsViewSet, basename='about-us')

urlpatterns = router.urls
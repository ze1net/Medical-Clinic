from django.urls import path, include
from rest_framework import routers

# diagnosis app called viewsets are
from .viewsets import DiagnosisHistoryViewSet, DiagnosisViewSet

router = routers.SimpleRouter()
router.register('d-history', DiagnosisHistoryViewSet, basename='diagnosis-histories')
router.register('diagnosis', DiagnosisViewSet, basename='diagnosis')

urlpatterns = router.urls
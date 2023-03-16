from rest_framework import viewsets, permissions, serializers
from rest_framework.generics import get_object_or_404

from user.models import UserModel
from .models import DiagnosisModel, DiagnosisHistoryModel
# diagnosis app called serializers are
from .serializers import DiagnosisHistoryModelSerializer, DiagnosisModelSerializer


# DiagnosisViewSet for DiagnosisModelSerializer
class DiagnosisViewSet(viewsets.ModelViewSet):
    serializer_class = DiagnosisModelSerializer
    permission_classes = [permissions.IsAuthenticated]


    def perform_create(self, serializer):
        # Retrieve the EmployeeModel instance associated with the authenticated user
        employee = self.request.user.employee.first()
        if employee:
            serializer.save(doctor=employee)
        else:
            raise serializers.ValidationError('The authenticated user is not associated with an employee.')

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

    # IntegrityError is prevented
    def get_queryset(self):
        queryset = DiagnosisModel.objects.filter(user=self.request.user.id)
        return queryset


# DiagnosisHistoryViewSet for DiagnosisHistoryModelSerializer
class DiagnosisHistoryViewSet(viewsets.ModelViewSet):
    queryset = DiagnosisHistoryModel.objects.all()
    serializer_class = DiagnosisHistoryModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAdminUser]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

    # IntegrityError is prevented
    def get_queryset(self):
        queryset = DiagnosisHistoryModel.objects.filter(user=self.request.user.id)
        return queryset

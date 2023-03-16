from rest_framework import serializers

from staff.models import EmployeeModel
from staff.serializers import EmployeeModelSerializer
# diagnosis app called models are
from .models import DiagnosisModel, DiagnosisHistoryModel


# DiagnosisModelSerializer for DiagnosisModel
class DiagnosisModelSerializer(serializers.ModelSerializer):
    diagnosis_history_name = serializers.SerializerMethodField()
    doctor_full_name = serializers.SerializerMethodField()
    user_full_name = serializers.SerializerMethodField()

    class Meta:
        model = DiagnosisModel
        fields = ['id', 'name', 'diagnosis', 'user', 'user_full_name', 'doctor', 'doctor_full_name',
                  'diagnosis_history', 'diagnosis_history_name']
        read_only_fields = ['doctor']

    def get_diagnosis_history_name(self, obj):
        return obj.diagnosis_history.name

    def get_doctor_full_name(self, obj):
        return obj.doctor.user.get_full_name

    def get_user_full_name(self, obj):
        return obj.user.get_full_name


# DiagnosisHistoryModelSerializer for DiagnosisHistoryModel
class DiagnosisHistoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosisHistoryModel
        fields = '__all__'

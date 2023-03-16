from ckeditor.fields import RichTextField
from django.db import models
from service.models import ServiceModel
from staff.models import EmployeeModel
from user.models import UserModel


class DiagnosisHistoryModel(models.Model):
    name = models.CharField(max_length=55)
    description = RichTextField()
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='diagnosis_history')
    service = models.ForeignKey(ServiceModel, on_delete=models.RESTRICT, related_name='diagnosis_history')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.get_full_name

    class Meta:
        verbose_name = 'diagnosis_history'
        verbose_name_plural = 'diagnosis_history'


class DiagnosisModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='diagnosis')
    doctor = models.ForeignKey(EmployeeModel, on_delete=models.RESTRICT, related_name='diagnosis')
    diagnosis_history = models.ForeignKey(DiagnosisHistoryModel, on_delete=models.CASCADE, related_name='diagnosis')
    name = models.CharField(max_length=55)
    diagnosis = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.diagnosis_history.user.get_full_name()} {self.name} {self.created_at.date()}'

    class Meta:
        verbose_name = 'diagnosis'
        verbose_name_plural = 'diagnosis'


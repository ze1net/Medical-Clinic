from django.db import models
# UserModel is called from our user app
from user.models import UserModel


# StaffCategoryModel for Staff Categories
class StaffCategoryModel(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name

    # to see it with a specific name in the admin panel
    class Meta:
        verbose_name = 'staff_category'
        verbose_name_plural = 'staff_categories'


# DirectionModel for employee directions
class DirectionModel(models.Model):
    staff_category = models.ForeignKey(StaffCategoryModel, on_delete=models.CASCADE, related_name='direction')
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name

    # to see it with a specific name in the admin panel
    class Meta:
        verbose_name = 'direction'
        verbose_name_plural = 'directions'


# EmployeeModel for employees
class EmployeeModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='employee')
    direction = models.ForeignKey(DirectionModel, on_delete=models.RESTRICT, related_name='employee')

    def __str__(self):
        return self.user.get_full_name

    # to see it with a specific name in the admin panel
    class Meta:
        verbose_name = 'employee'
        verbose_name_plural = 'employees'

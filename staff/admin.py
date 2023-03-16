from django.contrib import admin

# staff app called models are
from .models import StaffCategoryModel, DirectionModel, EmployeeModel


# StaffCategoryModelAdmin  for StaffCategoryModel
@admin.register(StaffCategoryModel)
class StaffCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']


# DirectionModelAdmin for DirectionModel
@admin.register(DirectionModel)
class DirectionModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'staff_category']
    list_display_links = ['id', 'name', 'staff_category']
    search_fields = ['name', 'staff_category']


# EmployeeModelAdmin  for  EmployeeModel
@admin.register(EmployeeModel)
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'direction']
    list_display_links = ['id', 'user', 'direction']
    search_fields = ['user', 'direction']

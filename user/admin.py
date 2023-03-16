from django.contrib import admin

# user app models are called
from user.models import UserModel, CountryModel, RegionModel, CityModel


# UserModelAdmin for UserModel
@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_full_name', 'username']
    list_display_links = ['id', 'get_full_name', 'username']
    search_fields = ['email', 'get_fullname', 'username']


# CountryModelAdmin for CountryModel
@admin.register(CountryModel)
class CountryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']


# RegionModelAdmin for RegionModel
@admin.register(RegionModel)
class RegionModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'country', 'name']
    list_display_links = ['id', 'country', 'name']
    search_fields = ['name', 'country']

# CityModelAdmin for CityModel
@admin.register(CityModel)
class CityModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'region', 'name']
    list_display_links = ['id', 'region', 'name']
    search_fields = ['name', 'region', ]

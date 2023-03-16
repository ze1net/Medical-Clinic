from django.db import models
from django.contrib.auth.models import AbstractUser


# CountryModel for ProfileModel's country field
class CountryModel(models.Model):
    name = models.CharField(max_length=55, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'country'
        verbose_name_plural = 'countries'


# RegionModel for CountryModel's region
class RegionModel(models.Model):
    country = models.ForeignKey(CountryModel, on_delete=models.CASCADE, related_name='region')
    name = models.CharField(max_length=55, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'region'
        verbose_name_plural = 'regions'


# CityModel for RegionModel's city
class CityModel(models.Model):
    region = models.ForeignKey(RegionModel, on_delete=models.CASCADE, related_name='city')
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'city'
        verbose_name_plural = 'cities'


# UserModel for User
class UserModel(AbstractUser):
    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


# ProfileModel for users to enter their profile information and view their profile
class ProfileModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile', unique=True)
    city = models.ForeignKey(CityModel, on_delete=models.RESTRICT, related_name='profile', null=True)
    address = models.CharField(max_length=255, null=True)
    zip_code = models.PositiveIntegerField(null=True)
    phone = models.CharField(max_length=16, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Selection part for gender
    # gender value
    M = 'Male'
    F = 'Female'
    # genders list
    genders = [
        (M, 'Male'),
        (F, 'Female'),
    ]

    # choice for gender selection function
    def gender_selector(self):
        return self.gender in {self.M, self.F}

    # gender field
    gender = models.CharField(max_length=20, choices=genders, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)

    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'

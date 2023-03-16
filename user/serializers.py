# Rest Framework serializer classes are used
from rest_framework import serializers
# user app models are called
from .models import UserModel, CountryModel, CityModel, RegionModel, ProfileModel


# CountryModelSerializer for the country field of the RegionModelSerializer
class CountryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryModel
        exclude = ['id']


# RegionModelSerializer for the country field of the CityModelSerializer
class RegionModelSerializer(serializers.ModelSerializer):
    # field to get the country name
    country_name = serializers.SerializerMethodField()

    class Meta:
        model = RegionModel
        fields = ['id', 'country', 'country_name', 'name']

    # function to get the country name
    def get_country_name(self, obj):
        return obj.country.name


# CityModelSerializer for the country field of the ProfileModelSerializer
class CityModelSerializer(serializers.ModelSerializer):
    # field to get the region name
    region_name = serializers.SerializerMethodField()

    class Meta:
        model = CityModel
        fields = ['id', 'region', 'region_name', 'name']

    # function to get the region name
    def get_region_name(self, obj):
        return obj.region.name


# for users to register
class UserSerializer(serializers.ModelSerializer):
    # field for user password
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        return user


# ProfileModelSerializer for users
class UserProfileSerializer(serializers.ModelSerializer):
    # field to get the city name
    city_name = serializers.SerializerMethodField()

    class Meta:
        model = ProfileModel
        fields = ['id', 'address', 'zip_code', 'phone', 'gender', 'age', 'city', 'city_name']

    # function to get the city name
    def get_city_name(self, obj):
        return obj.city.name

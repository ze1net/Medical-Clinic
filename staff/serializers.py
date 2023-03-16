# Rest Framework serializer classes are used
from rest_framework import serializers
# Staff called the models created to store their data
from .models import StaffCategoryModel, EmployeeModel, DirectionModel


# Created serializer class for StaffCategoryModel
class StaffCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffCategoryModel
        exclude = ['id']

    # def create(self, validated_data):
    #     return StaffCategoryModel.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data['name']
    #     instance.save()
    #     return instance


# Created serializer class for DirectionModel
class DirectionModelSerializer(serializers.ModelSerializer):
    # A variable is created to get the StaffCategoryModel`s name field  without nesting
    staff_category_name = serializers.SerializerMethodField()

    class Meta:
        model = DirectionModel
        fields = ['id', 'staff_category', 'staff_category_name', 'name']

    # A function is created to get the StaffCategoryModel`s name field  without nesting
    def get_staff_category_name(self, obj):
        return obj.staff_category.name


# Created serializer class for EmployeeModel
class EmployeeModelSerializer(serializers.ModelSerializer):
    direction_name = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = EmployeeModel
        fields = ['id', 'user', 'full_name', 'direction', 'direction_name']

    # A function is created to get the DirectionModel`s name field  without nesting
    def get_direction_name(self, obj):
        return obj.direction.name

    # A function is created to get the UserModel`s fullname  without nesting
    def get_full_name(self, obj):
        return f'{obj.user.first_name} {obj.user.last_name}'

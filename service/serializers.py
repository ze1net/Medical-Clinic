from rest_framework import serializers
from .models import ServiceCategoryModel, ServiceModel, ServiceCommentModel, ServiceTagModel


class ServiceTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceTagModel
        fields = '__all__'


class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategoryModel
        exclude = ['id']


class ServiceSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = ServiceModel
        fields = ['id', 'name', 'category', 'category_name', 'image', 'price', 'description', 'tags', 'created_at',
                  'updated_at', ]

    def get_category_name(self, obj):
        return obj.category.name


class ServiceCommentSerializer(serializers.ModelSerializer):
    service_name = serializers.SerializerMethodField()

    class Meta:
        model = ServiceCommentModel
        exclude = ['user']

    def get_service_name(self, obj):
        return obj.service.name

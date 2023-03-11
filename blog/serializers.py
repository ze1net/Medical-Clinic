from rest_framework import serializers
from .models import BlogModel, BlogCategoryModel, BlogCommentModel, BlogTagModel


class BlogCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategoryModel
        exclude = ['id']


class BlogTagModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogTagModel
        fields = '__all__'


class BlogModelSerializer(serializers.ModelSerializer):
    category = BlogCategoryModel()

    class Meta:
        model = BlogModel
        fields = ['id', 'category', 'title', 'image', 'description', 'tags']



class BlogCommentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCommentModel
        exclude = ['user']


from rest_framework import serializers

# blog app called  models are
from .models import BlogModel, BlogCategoryModel, BlogCommentModel, BlogTagModel


# BlogTagModelSerializer for BlogTagModel
class BlogTagModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogTagModel
        fields = '__all__'


# BlogCategoryModelSerializer for BlogCategoryModel
class BlogCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategoryModel
        exclude = ['id']


# BlogModelSerializer for BlogModel
class BlogModelSerializer(serializers.ModelSerializer):
    # a value for get category name
    category_name = serializers.SerializerMethodField()
    tags = serializers.SlugRelatedField(
        many=True,
        queryset=BlogTagModel.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = BlogModel
        fields = ['id', 'category', 'category_name', 'title', 'image', 'description', 'tags']

    # function for get category name
    def get_category_name(self, obj):
        return obj.category.name

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        blog = BlogModel.objects.create(**validated_data)
        for tag_data in tags_data:
            tag, created = BlogTagModel.objects.get_or_create(name=tag_data)
            blog.tags.add(tag)
        return blog

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags')
        instance = super().update(instance, validated_data)
        instance.tags.clear()
        for tag_data in tags_data:
            tag, created = BlogTagModel.objects.get_or_create(name=tag_data)
            instance.tags.add(tag)
        return instance


# BlogCommentModelSerializer for BlogCommentModel
class BlogCommentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCommentModel
        exclude = ['user']

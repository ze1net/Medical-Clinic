from django.contrib import admin

# blog app called models are
from .models import BlogModel, BlogCategoryModel, BlogCommentModel, BlogTagModel


# BlogCategoryModelAdmin for BlogModel
@admin.register(BlogModel)
class BlogCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'created_at']
    list_display_links = ['id', 'title', 'category', 'created_at']
    search_fields = ['title', 'description', 'category', 'tags']


# BlogCategoryModel for BlogCategoryModel
@admin.register(BlogCommentModel)
class BlogCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'blog', 'user']
    list_display_links = ['id', 'blog', 'user']
    search_fields = ['blog', 'user']


# BlogCategoryModelAdmin for BlogCategoryModel
@admin.register(BlogTagModel)
class BlogTagModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']

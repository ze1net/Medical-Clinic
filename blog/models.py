from django.db import models
from ckeditor.fields import RichTextField

from user.models import UserModel


# BlogCategoryModel for blogModel's category
class BlogCategoryModel(models.Model):
    name = models.CharField(max_length=55, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'blog_category'
        verbose_name_plural = 'blog_categories'


# BlogTagModel for blogModel's tags
class BlogTagModel(models.Model):
    name = models.CharField(max_length=55, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


class BlogModel(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(BlogCategoryModel, on_delete=models.CASCADE, related_name='blog')
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_image/', null=True, blank=True)
    tags = models.ManyToManyField(BlogTagModel, related_name='blog')

    def __str__(self):
        return f'{self.title} {self.category.name} {self.created_at}'

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'


# CommentModel for blog comment
class BlogCommentModel(models.Model):
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.blog.title}'

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

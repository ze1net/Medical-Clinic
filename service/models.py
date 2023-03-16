from ckeditor.fields import RichTextField
from django.db import models

from user.models import UserModel


class ServiceCategoryModel(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class ServiceTagModel(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


class ServiceModel(models.Model):
    name = models.CharField(max_length=105)
    category = models.ForeignKey(ServiceCategoryModel, on_delete=models.CASCADE, related_name='services')
    description = RichTextField()
    image = models.ImageField(upload_to='service/service_image/')
    price = models.PositiveBigIntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(ServiceTagModel, related_name='services')

    def __str__(self):
        return self.name

    def get_info(self):
        return f'{self.name} {self.category}, {self.price}'

    class Meta:
        verbose_name = 'service'
        verbose_name_plural = 'services'


class ServiceCommentModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='comment')
    service = models.ForeignKey(ServiceModel, on_delete=models.CASCADE, related_name='comments')
    message = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user} {self.service}'

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

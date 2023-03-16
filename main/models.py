from ckeditor.fields import RichTextField
from django.db import models
from rest_framework.exceptions import ValidationError


class AboutUsModel(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField()
    image = models.ImageField(upload_to='about_us_image/')
    is_information_added = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_information_added:
            # Only allow editing if information has been added
            super().save(*args, **kwargs)
        else:
            # Only allow one instance of the model to be created
            if not self.pk and AboutUsModel.objects.exists():
                raise ValidationError("Only one instance of AboutUsModel is allowed")
            self.is_information_added = True
            super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'about_us'
        verbose_name_plural = 'about_uses'


class ContactUsModel(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.created_at.date()}'

    class Meta:
        verbose_name = 'contact_us'
        verbose_name_plural = 'contact_uses'

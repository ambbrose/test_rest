from django.db import models
from django.core.validators import FileExtensionValidator

class Hero(models.Model):
    title = models.CharField(max_length=200, blank=True)
    subtitle = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to='hero_logo', blank=True, validators=[FileExtensionValidator(['png'])])
    is_active = models.BooleanField(default=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Hero'
        db_table = 'Hero'

# class HeroImages(models.Model):
#     image = models.ImageField(upload_to='hero_images')
#     thumbnail = models.ImageField(upload_to='hero_thumbnails', blank=True, null=True)
#     hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
#     is_active = models.BooleanField(default=True)
#     created_timestamp = models.DateTimeField(auto_now_add=True)
#     uploaded_timestamp = models.DateTimeField(auto_now=True)

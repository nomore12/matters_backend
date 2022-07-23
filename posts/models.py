from fileinput import filename
from this import d
from django.db import models
from datetime import datetime

# Create your models here.

post_type_choices = [
    ('residential', 'residential'),
    ('office', 'office'),
    ('commercial', 'commercial'),
    ('hospitality', 'hospitality'),
    ('exhibition', 'exhibition'),
    ('furniture', 'furniture'),
    ('unbuilt', 'unbuilt'),
    ('etc', 'etc'),
]

class Post(models.Model):
    title = models.CharField(max_length=128)
    sudtitle = models.CharField(max_length=256)
    location = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    from_date = models.DateField(auto_now=False, blank=True)
    to_date = models.DateField(auto_now=False, blank=True)
    description = models.TextField()
    main_image = models.ImageField(blank=True, upload_to="main")
    thumbnail = models.ImageField(blank=True, upload_to="thumbnail")
    post_type = models.CharField(max_length=32, choices=post_type_choices)
    image_list = models.TextField(blank=True)

    def __str__(self):
        return self.title


class ImageModel(models.Model):
    image = models.ImageField(blank=True, upload_to="main")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

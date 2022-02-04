from fileinput import filename
from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    main_image = models.ImageField(blank=True, upload_to="main")
    thumbnail = models.ImageField(blank=True, upload_to="thumbnail")
    post_type = models.CharField(max_length=32, default="none")

    # def save(self, *args, **kwargs):
    #     if self.main_image is not None:
    #         saved_image = self.main_image

    def __str__(self):
        return self.title

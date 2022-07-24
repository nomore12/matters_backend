from django.contrib import admin
from .models import Post, ImageModel


# @admin.register(ImageModel)
class ImageAdmin(admin.StackedInline):
    model = ImageModel

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'post_type', 'created_at', 'updated_at']
    link_display_link = ['title']
    exclude = ['main_image', 'image_list']
    list_search = ['title']
    list_filter = ['post_type']
    inlines = [
            ImageAdmin,
        ]

from django.contrib import admin
from .models import Post, ImageModel
from django.utils.html import format_html


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

    def image_tag(self, obj):
        return format_html('<img src="http://localhost:8000/media/{}" width="50px" />'.format(obj.thumbnail))
    
    image_tag.short_description = 'Image'

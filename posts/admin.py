from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'post_type', 'description', 'created_at', 'updated_at', 'main_image']
    link_display_link = ['title']
    list_search = ['title']
    list_filter = ['post_type']
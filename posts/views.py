from django.http import HttpResponse
from .models import Post, ImageModel
from django.core import serializers


def get_post_lists(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        json_post = serializers.serialize('json', posts)
        return HttpResponse(json_post)


def get_post(request, post_id):
    if request.method == 'GET':
        post = Post.objects.filter(pk=post_id)
        images = ImageModel.objects.filter(post=post_id)
        json_post = serializers.serialize('json', post)
        image_posts = serializers.serialize('json', images)
        return HttpResponse(json_post)


def get_detail_images(request, post_id):
    if request.method == 'GET':
        images = ImageModel.objects.filter(post=post_id)
        json_images = serializers.serialize('json', images)
        return HttpResponse(json_images)
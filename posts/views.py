import imghdr
from pipes import Template
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Post, ImageModel
from django.conf import settings
from django.core import serializers
import json


def get_post_lists(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        json_post = serializers.serialize('json', posts)
        return HttpResponse(json_post)


def get_post(request, post_id):
    if request.method == 'GET':
        post = Post.objects.filter(pk=post_id)
        images = list(ImageModel.objects.filter(post=post_id).values())
        # images_json = serializers.serialize('json', images)
        # post_images = serializers.serialize('json',images)
        json_post = serializers.serialize('json', post)
        
        print(images, json_post)
        print(type(json_post))
        
        result = json.loads(json_post)
        print(type(json_post))
        print(result)
        
        return HttpResponse(json_post)

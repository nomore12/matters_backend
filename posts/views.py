from pipes import Template
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Post
from django.conf import settings
from django.core import serializers


def get_post_lists(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        json_post = serializers.serialize('json', posts)
        return HttpResponse(json_post)


def get_post(request, post_id):
    if request.method == 'GET':
        print(request, post_id)
        post = Post.objects.filter(pk=post_id)
        json_post = serializers.serialize('json', post)
        print(f"json {json_post}")
        return HttpResponse(json_post)

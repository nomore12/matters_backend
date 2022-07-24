from django.urls import path
from . import views

urlpatterns = [
    path('<int:post_id>/', views.get_post),
    path('images/<int:post_id>/', views.get_detail_images),
    path('', views.get_post_lists),
]
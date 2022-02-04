from django.urls import path
from . import views

urlpatterns = [
    path('<int:post_id>/', views.get_post),
    path('', views.get_post_lists),
]
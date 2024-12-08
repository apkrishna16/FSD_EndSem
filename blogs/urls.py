from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('blogs_content/<int:blog_id>/', views.blog_content, name='blog_content'),
]
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

router = DefaultRouter()
router.register('userpost', views.UserPostViewSet, basename='userpost')

urlpatterns = [
    path('',include(router.urls)),
#     path('post/', views.PostList.as_view()),
#     path('post/<int:pk>', views.PostDetail.as_view()),
]
from django.contrib import admin
from django.urls import path,include
from . import views
app_name='post'
urlpatterns = [
    path('memos/',views.PostList.as_view(),name='list'),
    path('memos/<int:pk>/',views.PostDelail.as_view(),name='detail'),
    path('memos/create',views.CreatePost.as_view(),name='create')


]

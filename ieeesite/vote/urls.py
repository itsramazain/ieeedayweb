from django.contrib import admin
from django.urls import path,include
from . import views
app_name='vote'
urlpatterns = [
    path('',views.vote,name='vote2'),
    path('results/',views.results,name='results')


]

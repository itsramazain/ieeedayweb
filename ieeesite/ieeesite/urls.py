"""ieeesite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.HomePgae.as_view(),name='home'),
    path('accounts/',include('accounts.urls',namespace="accounts")),
    path('thanks/',views.Thanks.as_view(),name="thanks"),
    path('logg/',views.Logg.as_view(),name='logg'),
    path('post/',include('post.urls',namespace="post")),
    path('vote/',include('vote.urls',namespace="vote"))
]

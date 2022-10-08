from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.utils import timezone
User=get_user_model()
from django import template
register=template.library
# Create your models here.
class Socity(models.Model):
    socity=models.CharField(max_length=200)
    def __str__(self):
        return self.socity
class rate(models.Model):
    rate=models.CharField(max_length=200)
    def __str__(self):
        return self.rate
class Group(models.Model):
    group=models.CharField(max_length=200)
    def __str__(self):
        return self.group

class Post(models.Model):
    stars=models.ForeignKey(rate,on_delete=models.CASCADE)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    group=models.ForeignKey(Group,on_delete=models.CASCADE)
    position=models.CharField(max_length=200,blank=True)
    massage=models.TextField(blank=True,default='')
    time=models.DateTimeField(default=timezone.now)
    to=models.ForeignKey(Socity,on_delete=models.CASCADE)
    def __str__(self):
        return self.author.username
    def save(self,*args,**kwagrs):
        super().save(*args,**kwagrs)
    def get_absolute_url(self):
        return reverse('post:list')
    def has_related_object(self):
        return self.author

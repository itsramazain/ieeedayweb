from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
from post.models import Post
from django.views import generic
from django.http import Http404
from braces.views import SelectRelatedMixin
from post.forms import PostForm
from django.utils import timezone
from django.contrib.auth import get_user_model
User=get_user_model()
# Create your views here.
class PostList(generic.ListView):
    template_name='post/list.html'
    context_object_name='posts'
    model=Post
    def get_queryset(self):
        return Post.objects.filter(time__lte=timezone.now()).order_by('-time')
class CreatePost(LoginRequiredMixin,generic.CreateView):
    template_name='post/create.html'
    form_class= PostForm
    model=Post
    context_object_name='posts'
    success_url=reverse_lazy('post:list')
    def form_valid(self,PostForm):
        PostForm.instance.author = self.request.user
        return super().form_valid(PostForm)


class PostDelail(generic.DetailView):
    template_name='post/detail.html'
    context_object_name='witer'
    model=Post

from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from posts.models import Post
from posts.serializers import PostSerializer


class IndexPage(TemplateView):
    template_name = 'index.html'

'''
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

'''

class PostList(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)


from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, TemplateView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers
from .models import Post

# Create your views here.


class HomePageView(ListView):
    model = Post
    paginate_by = 9
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginate_page_range = context['page_obj'].paginator.num_pages
        all_promote_posts = Post.objects.filter(promote=True)
        context['paginate_page_range'] = range(1, paginate_page_range + 1)
        context['all_promote_posts'] = all_promote_posts
        return context


class ContactPageView(TemplateView):
    template_name = 'blog/page-contact.html'


class AllPostsAPIView(generics.ListAPIView):
    queryset = Post.objects.all().order_by('-updated_at')
    serializer_class = serializers.AllPostsSerializer


class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostDetailSerializer


class PostSearchAPIView(generics.ListAPIView):
    serializer_class = serializers.AllPostsSerializer

    def get_queryset(self):
        from django.db.models import Q
        query = self.request.GET['query']
        return Post.objects.filter(Q(title__icontains=query) | Q(body__icontains=query)).order_by('-updated_at')


class PostCreateAPIView(generics.CreateAPIView):
    model = Post
    serializer_class = serializers.PostCreateSerializer


class PostUpdateAPIView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostUpdateSerializer


class PostDeleteAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()

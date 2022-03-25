from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView
from .models import Post
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from .serializers import AllPostsSerializer, PostDetailSerializer, PostCreateSerializer, PostUpdateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
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


class AllPostsAPIView(ListAPIView):
    queryset = Post.objects.all().order_by('-updated_at')
    serializer_class = AllPostsSerializer


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class PostSearchAPIView(ListAPIView):
    serializer_class = AllPostsSerializer

    def get_queryset(self):
        from django.db.models import Q
        query = self.request.GET['query']
        return Post.objects.filter(Q(title__icontains=query) | Q(body__icontains=query)).order_by('-updated_at')    


class PostCreateAPIView(CreateAPIView):
    model = Post
    serializer_class = PostCreateSerializer


class PostUpdateAPIView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer

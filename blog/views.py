from django.shortcuts import render
from django.views.generic import ListView, TemplateView
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

from django.urls import path
from .views import HomePageView, ContactPageView, AllPostsAPIView

app_name = 'blog'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contact/', ContactPageView.as_view(), name='contact'),

    # apis
    path('api/post/all/', AllPostsAPIView.as_view(), name='all-posts'),
]

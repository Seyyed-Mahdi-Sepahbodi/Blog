from django.urls import path
from .views import HomePageView, ContactPageView, AllPostsAPIView, PostDetailAPIView, PostSearchAPIView, PostCreateAPIView

app_name = 'blog'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contact/', ContactPageView.as_view(), name='contact'),

    # apis
    path('api/post/all/', AllPostsAPIView.as_view(), name='all-posts'),
    path('api/post/<int:pk>/', PostDetailAPIView.as_view(), name='detail-post'),
    path('api/post/search/', PostSearchAPIView.as_view(), name='search-post'),
    path('api/post/create/', PostCreateAPIView.as_view(), name='create-post'), 
]

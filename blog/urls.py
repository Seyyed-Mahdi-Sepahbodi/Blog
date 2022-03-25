from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('contact/', views.ContactPageView.as_view(), name='contact'),

    # apis
    path('api/post/all/', views.AllPostsAPIView.as_view(), name='all-posts'),
    path('api/post/<int:pk>/', views.PostDetailAPIView.as_view(), name='detail-post'),
    path('api/post/search/', views.PostSearchAPIView.as_view(), name='search-post'),
    path('api/post/create/', views.PostCreateAPIView.as_view(), name='create-post'),
    path('api/post/<int:pk>/update/', views.PostUpdateAPIView.as_view(), name='update-post'),
    path('api/post/<int:pk>/delete/', views.PostDeleteAPIView.as_view(), name='delete-post'),
]

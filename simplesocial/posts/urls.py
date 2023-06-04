from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path(r'', views.PostList.as_view(), name='all'),
    path('new/', views.CreatePost.as_view(), name='create'),
    # path(r'by/(username[-\w]+)/', views.UserPosts.as_view(), name='for_user'),
    path(r'by/(?P<username>[-\w]+)/', views.UserPosts.as_view(), name='for_user'),
    path(r'by/(username[-\w]+)/(pk\d)/', views.PostDetail.as_view(), name='single'),
    path(r'delete/(pk\d)/', views.DeletePost.as_view(), name='delete'),
]

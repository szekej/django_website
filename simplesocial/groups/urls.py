from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path(r'', views.ListGroup.as_view(), name='all'),
    path(r'new/', views.CreateGroup.as_view(), name='create'),
    path(r'posts/in/(slug[-\w]+)/', views.SingleGroup.as_view(), name='single'),
    path(r'join/(slug[-\w]+)/', views.JoinGroup.as_view(), name='join'),
    path(r'leave/(slug[-\w]+)/', views.LeaveGroup.as_view(), name='leave'),
]
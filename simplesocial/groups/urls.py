from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path(r'', views.ListGroup.as_view(), name='all'),
    path(r'new/', views.CreateGroup.as_view(), name='create'),
    path('posts/in/<slug:slug>/', views.SingleGroup.as_view(), name='single'),
    path(r'join/<slug:slug>/', views.JoinGroup.as_view(), name='join'),
    path(r'leave/<slug:slug>/', views.LeaveGroup.as_view(), name='leave'),
]
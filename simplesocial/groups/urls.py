from django.urls import path
from . import views

app_name = 'groups'

url_patterns = [
    path(r'', views.ListGroup.as_view(), name='all'),
    path(r'new/', views.CreateGroup.as_view(), name='create'),
    path(r'posts/in/(?P<slug>[-\w]+)/', views.SingleGroup.as_view(), name='single')

]
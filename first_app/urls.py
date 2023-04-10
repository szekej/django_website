from django.urls import path
from first_app import views

# TEMPLATE TAGGING
app_name = 'first_app'

urlpatterns = [
    # path(r'^first_app', include('first_app.urls')),
    path(r'relative', views.relative, name='relative'),
    path(r'myextension', views.myextension, name='myextension'),
    path(r'mtv', views.mtv, name='mtv'),
    path(r'users', views.users, name='users'),
    path(r'new_user', views.new_user, name='new_user'),
    path(r'formpage', views.form_name_view, name='formname'),
    path(r'register', views.register, name='register'),
    path(r'user_login', views.user_login, name='user_login')
    # path('admin/', admin.site.urls),
]

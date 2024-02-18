# password_manager/urls.py
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import base, site_list, add_site, edit_site, delete_site, register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('base/', base, name='base'),
    path('sites/', site_list, name='site_list'),
    path('add/', add_site, name='add_site'),
    path('edit/<int:site_id>/', edit_site, name='edit_site'),
    path('delete/<int:site_id>/', delete_site, name='delete_site'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # ... autres vues
]

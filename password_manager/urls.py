# password_manager/urls.py
from django.urls import path
from .views import base, site_list, add_site, edit_site, delete_site

urlpatterns = [
    path('base/', base, name='base'),
    path('sites/', site_list, name='site_list'),
    path('add/', add_site, name='add_site'),
    path('edit/<int:site_id>/', edit_site, name='edit_site'),
    path('delete/<int:site_id>/', delete_site, name='delete_site'),
]

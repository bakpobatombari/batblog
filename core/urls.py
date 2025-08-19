from django.urls import path
from django.contrib.auth import views as auth_views

from .forms import LoginForm
from . import views, views_admin

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register, name="register"),
    path('about/', views.about, name="about"),
    path('about/forms/', views.aboutContent, name="Content Page"),
    path('login/',auth_views.LoginView.as_view(template_name='core/login.html',authentication_form=LoginForm), name = 'login'),
    path('logout/', views.logout_view, name='logout'),
    # Admin dashboard user management
    path('bat/admin/users/', views_admin.user_list, name='admin_user_list'),
    path('accounts/profile/', views.index),
    path('bat/admin/users/add/', views_admin.user_add, name='admin_user_add'),
    path('bat/admin/users/<int:user_id>/edit/', views_admin.user_edit, name='admin_user_edit'),
    path('bat/admin/users/<int:user_id>/delete/', views_admin.user_delete, name='admin_user_delete'),
    path('bat/admin/users/<int:user_id>/barn/', views_admin.user_barn, name='admin_user_barn'),
]

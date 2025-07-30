from django.urls import path

from . import views, views_admin

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register, name="register"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # Admin dashboard user management
    path('bat/admin/users/', views_admin.user_list, name='admin_user_list'),
    path('bat/admin/users/add/', views_admin.user_add, name='admin_user_add'),
    path('bat/admin/users/<int:user_id>/edit/', views_admin.user_edit, name='admin_user_edit'),
    path('bat/admin/users/<int:user_id>/delete/', views_admin.user_delete, name='admin_user_delete'),
    path('bat/admin/users/<int:user_id>/barn/', views_admin.user_barn, name='admin_user_barn'),
]

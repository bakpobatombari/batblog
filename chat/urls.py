from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_room_list, name='chat_room_list'),
    path('room/<int:room_id>/', views.chat_room, name='chat_room'),
    path('start/<int:user_id>/', views.start_chat, name='start_chat'),
]

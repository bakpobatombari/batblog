from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import ChatRoom, Message
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@login_required
def chat_room_list(request):
    rooms = ChatRoom.objects.filter(participants=request.user)
    User = get_user_model()
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'chat/room_list.html', {'rooms': rooms, 'users': users})

@login_required
def chat_room(request, room_id):
    room = get_object_or_404(ChatRoom, id=room_id, participants=request.user)
    messages = room.messages.order_by('timestamp')
    return render(request, 'chat/room.html', {'room': room, 'messages': messages})

@login_required
def start_chat(request, user_id):
    User = get_user_model()
    other_user = get_object_or_404(User, id=user_id)
    if other_user == request.user:
        return redirect('chat_room_list')
    # Find or create a room with these two users
    rooms = ChatRoom.objects.filter(participants=request.user).filter(participants=other_user)
    if rooms.exists():
        room = rooms.first()
    else:
        room = ChatRoom.objects.create()
        room.participants.add(request.user, other_user)
    return redirect('chat_room', room_id=room.id)

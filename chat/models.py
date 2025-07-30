from django.db import models
from django.contrib.auth import get_user_model

class ChatRoom(models.Model):
    participants = models.ManyToManyField(get_user_model(), related_name='chatrooms')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Room {self.id}"  # or list of usernames

class Message(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}: {self.content[:30]}..."

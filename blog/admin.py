from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "author", "created_at")
    search_fields = ("title", "content", "author__username")
    list_filter = ("created_at", "author")

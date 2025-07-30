from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify

def blog_list(request):
    posts = BlogPost.objects.order_by('-created_at')
    return render(request, 'blog/blog_list.html', {'posts': posts})

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'blog/blog_detail.html', {'post': post})

@login_required
def blog_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.slug = slugify(blog.title)
            blog.save()
            return redirect('blog_detail', slug=blog.slug)
    else:
        form = BlogPostForm()
    return render(request, 'blog/blog_form.html', {'form': form})

@login_required
def blog_edit(request, slug):
    blog = get_object_or_404(BlogPost, slug=slug)
    if request.user != blog.author and not request.user.is_staff:
        return redirect('blog_detail', slug=slug)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.slug = slugify(blog.title)
            blog.save()
            return redirect('blog_detail', slug=blog.slug)
    else:
        form = BlogPostForm(instance=blog)
    return render(request, 'blog/blog_form.html', {'form': form, 'edit': True})

@login_required
def blog_delete(request, slug):
    blog = get_object_or_404(BlogPost, slug=slug)
    # Allow only the author or an admin to delete
    if not (request.user == blog.author or request.user.is_staff):
        return redirect('blog_detail', slug=slug)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')
    return render(request, 'blog/blog_confirm_delete.html', {'blog': blog})

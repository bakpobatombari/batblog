
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms_admin import UserEditForm, UserCreateForm
from django.contrib import messages

def admin_required(view_func):
    return user_passes_test(lambda u: u.is_staff)(view_func)

@admin_required
def user_barn(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == "POST":
        user.is_active = False
        user.save()
        messages.success(request, f"User '{user.username}' has been barned (deactivated).")
        return redirect("admin_user_list")
    return redirect("admin_user_list")

@admin_required
def user_list(request):
    users = User.objects.all()
    return render(request, "core/admin_user_list.html", {"users": users})

@admin_required
def user_add(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User created successfully.")
            return redirect("admin_user_list")
    else:
        form = UserCreateForm()
    return render(request, "core/admin_user_form.html", {"form": form, "action": "Add"})

@admin_required
def user_edit(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == "POST":
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "User updated successfully.")
            return redirect("admin_user_list")
    else:
        form = UserEditForm(instance=user)
    return render(request, "core/admin_user_form.html", {"form": form, "action": "Edit"})

@admin_required
def user_delete(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == "POST":
        user.delete()
        messages.success(request, "User deleted successfully.")
        return redirect("admin_user_list")
    return render(request, "core/admin_user_confirm_delete.html", {"user": user})

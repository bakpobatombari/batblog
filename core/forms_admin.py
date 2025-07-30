from django import forms
from django.contrib.auth.models import User

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "is_active", "is_staff"]

class UserCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["username", "email", "password", "is_active", "is_staff"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

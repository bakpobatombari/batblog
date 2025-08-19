from django import forms
from django.contrib.auth.models import User

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "is_active", "is_staff"]
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Edit Username',
        'class': 'w-full py-4 bg-gray-700 px-6 rounded-xl'
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Edit Email',
        'class': 'w-full bg-gray-700 py-4 px-6 rounded-xl'
    }))

class UserCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["username", "email", "password", "is_active", "is_staff"]
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',
        'class': 'w-full py-4 bg-gray-700 px-6 rounded-xl'
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Email',
        'class': 'w-full bg-gray-700 py-4 px-6 rounded-xl'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 bg-gray-700 px-6 rounded-xl'
    }))
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

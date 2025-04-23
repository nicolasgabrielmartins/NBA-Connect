from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    bio = forms.CharField(widget=forms.Textarea, required=False)
    favorite_team = forms.CharField(max_length=100, required=False)
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'bio', 'favorite_team']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            # Salva o perfil com bio e favorite_team
            user.userprofile.bio = self.cleaned_data['bio']
            user.userprofile.favorite_team = self.cleaned_data['favorite_team']
            user.userprofile.save()
        return user

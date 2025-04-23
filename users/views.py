from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

@login_required
def profile_page(request):
    return render(request, 'users/profile.html', {
        'user': request.user,
        'profile': request.user.userprofile
        })
    

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            avatar = form.cleaned_data.get('avatar')
            if avatar:
                profile = user.userprofile
                profile.avatar = avatar
                profile.save()
            login(request, user)
            return redirect('profile-page')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})
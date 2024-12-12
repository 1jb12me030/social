from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            # Authenticate the user to determine the backend
            authenticated_user = authenticate(
                request, username=user.username, password=form.cleaned_data['password1']
            )
            if authenticated_user is not None:
                # Specify the backend explicitly
                login(request, authenticated_user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('users:profile')  # Redirect to the profile or any other page
            else:
                return render(request, 'users/register.html', {'form': form, 'error': 'Authentication failed.'})
    else:
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {'form': form})




@csrf_exempt
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard:index')  # Redirect to dashboard after login
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('users:login')  # Redirect to login page after logout
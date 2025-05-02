from django.shortcuts import render, redirect
from .forms import SignUpForm, CustomLoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful.")
                return redirect('accounts:login_view')  # Redirect to a success page.
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = CustomLoginForm()

    return render(request, 'accounts/login_view.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, "Logout successful.")
    return redirect('accounts/login_view.html')  # Redirect to a success page.

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Sign up successful.")
            return redirect('accounts/login_view.html')  # Redirect to a success page.
    else:
        form = SignUpForm()

    return render(request, 'accounts/signup_view.html', {'form': form})
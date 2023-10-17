from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from UserProfile.models import Cart, Profile

# Create your views here.
def index(request):
    # show user details if logged in
    if request.user.is_anonymous:
        return redirect("login")
    elif request.user.is_superuser:
        return redirect("administrator_index")
    else:
        return redirect("homepage")

def handle_signup(request):
    if request.method == 'POST' and request.POST['signup-btn']:
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        try:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            login(request, user)
            cart = Cart.objects.create(user=user)
            cart.save()
            profile = Profile.objects.create(user=user)
            profile.save()
            return redirect("user-profile")
        except IntegrityError:
            return render(request, "Authentication/signup.html", context={'error': True})
    else:
        return render(request, "Authentication/signup.html")


def handle_login(request):
    if request.method == 'POST' and request.POST['login-btn']:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("administrator_index") if user.is_superuser else redirect("homepage")
        else:
            return render(request, "Authentication/login.html", context={'error': True})
    else:
        return render(request, "Authentication/login.html")

def handle_logout(request):
    logout(request)
    return redirect("login")

def authenticate_user(username, password):
    return authenticate(username=username, password=password)
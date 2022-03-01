from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    # show user details if logged in
    if request.user.is_anonymous:
        return redirect("login")

    context = {
        'user': {
            'username': request.user.username
            # add other details
        }
    }
    return render(request, "authentication/index.html", context)

def handle_signup(request):
    if request.method == 'POST' and request.POST['signup-btn']:
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.create_user(username=username, password=password)
        user.save()
        login(request, user)
        return redirect("user_profile")
    else:
        return render(request, "Authentication/signup.html")


def handle_login(request):
    # print('r' in request.GET)
    if request.method == 'POST' and request.POST['login-btn']:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("administrator_index") if user.is_superuser else redirect("homepage")
        else:
            return render(request, "Authentication/login.html")
    else:
        return render(request, "Authentication/login.html")

def handle_logout(request):
    logout(request)
    return redirect("login")
 
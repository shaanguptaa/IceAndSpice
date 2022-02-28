from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):

    if request.user.is_anonymous:
        return redirect("administrator_login")

    context = {
        'user': {
            'username': request.user.username
        }
    }
    return render(request, "administrator/index.html", context)

def handle_admin_signup(request):
    if request.method == 'POST' and request.POST['signup-btn']:
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect("administrator_index")
    else:
        return render(request, "administrator/signup.html")


def handle_admin_login(request):
    if request.method == 'POST' and request.POST['login-btn']:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect("administrator_index")
        else:
            return redirect("administrator_login")
    else:
        return render(request, "administrator/login.html")

def handle_admin_logout(request):
    logout(request)
    return redirect("administrator_login")

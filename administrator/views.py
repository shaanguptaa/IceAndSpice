from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from Menu.views import get_all_items

# Create your views here.
def index(request):

    if request.user.is_anonymous or not request.user.is_superuser:
        return redirect("homepage")

    context = {
        'menu': get_all_items(),
    }
    return render(request, "administrator/index.html", context)

# def handle_admin_signup(request):
#     if request.method == 'POST' and request.POST['signup-btn']:
#         username = request.POST['username']
#         password = request.POST['password']

#         user = User.objects.create_user(username=username, password=password)
#         user.save()
#         return redirect("administrator_index")
#     else:
#         return render(request, "administrator/signup.html")


def handle_admin_login(request):
    if request.method == 'POST' and request.POST['login-btn']:
        username = request.POST['username'] 
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("administrator_index") if user.is_superuser else redirect("homepage")
        else:
            return redirect("login")
    else:
        return redirect("login")

def handle_admin_logout(request):
    logout(request)
    return redirect("login")

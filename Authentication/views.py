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

    # orders = get_orders(request)
    # # for i in range(len(orders)):
    # #     orders[i].items = orders[i].items.all()
    # context = {
    #     'user': {
    #         'username': request.user.username,
    #         # add other details
    #     },
    #     'orders': orders,
    #     'cart': get_cart(request),
    #     'reservations': get_reservations(request),
    # }
    # # orders = get_orders(request)
    # return render(request, "authentication/index.html", context)

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
            return redirect("user-profile") # later change it to user profile page .................................
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

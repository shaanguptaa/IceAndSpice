from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from Menu.models import Cart, Order
from Reservation.models import Reservation

# Create your views here.
def index(request):
    # show user details if logged in
    if request.user.is_anonymous:
        return redirect("login")

    orders = get_orders(request)
    # for i in range(len(orders)):
    #     orders[i].items = orders[i].items.all()
    context = {
        'user': {
            'username': request.user.username,
            # add other details
        },
        'orders': orders,
        'cart': get_cart(request),
        'reservations': get_reservations(request),
    }
    # orders = get_orders(request)
    return render(request, "authentication/index.html", context)

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
            return redirect("homepage") # later change it to user profile page .................................
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

def get_orders(request):
    orders = Order.objects.filter(user=request.user)

    orders = [{'id': order.id, 'items': [item for item in order.items.all()]} for order in orders.all()]

    return orders

def get_cart(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = {'items': [item for item in cart.items.all()], 'total': cart.total_amount}

    return cart_items

 
def get_reservations(request):
    if not request.user.is_authenticated:
        reservations, status = None, False
    else:
        reservations = Reservation.objects.filter(user=request.user)
        # print(reservations)

        # reservations = [x for x in reservations.values()] or None
        # print(reservations)
    #     status = True

    return reservations

    # return JsonResponse({'reservations': reservations, 'status': status})
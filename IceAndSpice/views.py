from django.shortcuts import render
from Menu.views import getmenu
from UserProfile.views import get_cart_for_homepage
from django.contrib.auth.models import User
from UserProfile.models import Cart

# Create your views here.
def index(request):
    init_carts()
    context = {
        'menu': getmenu(),
        'cartItems': get_cart_for_homepage(request.user) if not request.user.is_anonymous else None,
    }
    return render(request, 'IceAndSpice/index.html', context=context)

def init_carts():
    for user in User.objects.all():
        cart = Cart.objects.get_or_create(user=user)
        print(cart)

def temp(request):
    return render(request, 'IceAndSpice/temp.html', context=getmenu())
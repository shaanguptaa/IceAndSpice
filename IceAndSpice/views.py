from django.http import JsonResponse
from django.shortcuts import render
from Menu.views import getmenu
from UserProfile.views import get_cart_for_homepage
from django.contrib.auth.models import User
from UserProfile.models import Cart
from administrator.models import Feedback
from administrator.views import get_offers

# Create your views here.
def index(request):
    # init_carts()
    context = {
        'menu': getmenu(),
        'cartItems': get_cart_for_homepage(request.user) if not request.user.is_anonymous else None,
        'offers': get_offers(expired=False),
    }
    return render(request, 'IceAndSpice/index.html', context=context)

def init_carts():
    for user in User.objects.all():
        cart = Cart.objects.get_or_create(user=user)
        print(cart)

# def temp(request):
#     return render(request, 'IceAndSpice/temp.html', context=getmenu())

def add_feedback(request):
    if not request.user.is_authenticated:
        return JsonResponse({})
    elif request.method == 'POST' and request.POST['feedback']:
        try:
            name = request.POST['name']
            email = request.POST['email']
            message = request.POST['message']

            Feedback.objects.create(user=request.user, name=name, email=email, message=message)
            
            return JsonResponse({'status': 'Success'})

        except Exception as e:
            return JsonResponse({'status': 'Failed', 'error': e})
    
    return JsonResponse({})
    
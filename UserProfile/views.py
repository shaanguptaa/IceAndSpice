from django.http import JsonResponse
from django.shortcuts import redirect, render
from Menu.models import Menu
from Order.views import get_orders
# from Reservation.models import Reservation
from Reservation.views import get_reservations
from UserProfile.models import Cart, CartItem

# Create your views here.
def index(request):
    # show user details if logged in
    if request.user.is_anonymous:
        return redirect("login")

    orders = get_orders(request)
    # for i in range(len(orders)):
    #     orders[i].items = orders[i].items.all()
    context = {
        'user': request.user,
        'orders': orders,
        'cart': get_cart(request),
        'reservations': get_reservations(request),
    }
    # orders = get_orders(request)
    return render(request, "UserProfile/index.html", context)


def get_cart(request):
    cart = Cart.objects.get_or_create(user=request.user)[0]
    cart_items = {'items': [item for item in cart.items.all()], 'total': cart.total_amount}

    return cart_items

def add_to_cart(request):
    cart = Cart.objects.get_or_create(user=request.user)[0]
    item = request.POST['item']
    item = Menu.objects.get(id=item)
    quantity = int(request.POST['quantity'])
    # print(type(quantity))
    amount = quantity * item.price
    cartItem = CartItem.objects.create(item=item, quantity=quantity, amount=amount)
    # cartItem.save()

    cart.items.add(cartItem)

    return JsonResponse({'status': True})

def remove_from_cart(request):
    cart = Cart.objects.get_or_create(user=request.user)[0]
    item = request.POST['item']
    item = Menu.objects.get(id=item)
    items = [item for item in cart.items.filter(item=item)]
    # print(items)
    items = tuple(items)
    for item in items:
        cart.items.remove(item.id)
        item.delete()
    cart.save()

    return JsonResponse({'status': True})

def get_cart_for_homepage(user):
    cart = Cart.objects.get(user=user)
    data = [item.item.id for item in cart.items.all()]
    return data

# Commented in IceAndSpice/index.html AJAX Code for getting cart items also commented on urls of this app
# def get_cart_items(request):
#     cart = Cart.objects.get(user=request.user)
#     data = {
#         'items': dict(),
#         # 'status': True,
#         # 'quantity': dict(),
#     }

#     for item in cart.items.all():
#         data['items'][item.item.id] = item.quantity

#     data['status'] = True

#     return JsonResponse(data)
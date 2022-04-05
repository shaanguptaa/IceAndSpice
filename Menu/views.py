from django.http import JsonResponse
from django.shortcuts import render
from Menu.models import CartItem, Menu, Order, Cart
# Create your views here.

# def menu(request):
#     context = {
#         'menu': {
#             'main': Menu.objects.filter(category__iexact='Main'),
#             'drinks': Menu.objects.filter(category__iexact='Drinks'),
#             'dessert': Menu.objects.filter(category__iexact='Dessert')
#         },
#         'state': "done"
#     }

#     return render(request, 'Menu/menu.html', context=context)

def getmenu(category=[]):

    # k = [Menu.objects.values("category")]
    # print(k)
    data = {
        'main': [item for item in Menu.objects.filter(category='Main').values()] or None,
        'drinks': [x for x in Menu.objects.filter(category='Drinks').values()] or None,
        'desserts': [x for x in Menu.objects.filter(category='Desserts').values()] or None,
    }

    return data


def order(request):
    name = request.POST['personName']
    contact = request.POST['phone']
    address = request.POST['location']
    itemName = request.POST['itemName']
    total = request.POST['total']
    items = [item for item in Menu.objects.filter(item_name=itemName)]

    order = Order(name=name, contact=contact, total_amount=total, address=address, user=request.user)
    order.save()
    order.items.set(items)

    return JsonResponse({"status": True})

# def order_items(user):
#     # for ordering all items in cart
#     # need to add quantity along with the items
#     orders = [i for i in Order.objects.filter(user=user)]
#     items = []
#     for order in orders:
#         for item in order.items.all():
#             items.append(item)
#     data = {
#         'success': True,
#         'items': items,
#     }
#     print(items)
#     return data



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

def get_cart(user):
    cart = Cart.objects.get(user=user)
    data = [item.item.id for item in cart.items.all()]
    return data

def get_cart_items(request):
    cart = Cart.objects.get(user=request.user)
    data = {
        'items': dict(),
        # 'status': True,
        # 'quantity': dict(),
    }

    for item in cart.items.all():
        data['items'][item.item.id] = item.quantity

    data['status'] = True

    return JsonResponse(data)
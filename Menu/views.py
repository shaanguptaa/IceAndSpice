from django.http import JsonResponse
from django.shortcuts import render
from Menu.models import Menu, Order
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
        'menu': {
            'main': [item for item in Menu.objects.filter(category='Main').values()] or None,
            'drinks': [x for x in Menu.objects.filter(category='Drinks').values()] or None,
            'desserts': [x for x in Menu.objects.filter(category='Desserts').values()] or None,
        },
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

def order_items(user):
    # need to add quantity along with the items
    orders = [i for i in Order.objects.filter(user=user)]
    items = []
    for order in orders:
        for item in order.items.all():
            items.append(item)
    data = {
        'success': True,
        'items': items,
    }
    print(items)
    return data
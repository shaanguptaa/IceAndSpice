from django.http import JsonResponse
from Menu.models import Menu
from Order.models import Order

# Create your views here.
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

def get_orders(request):
    orders = Order.objects.filter(user=request.user)
    orders = [{
        'id': order.id,
        'items': ", ".join([item.item.item_name + ' x ' + str(item.quantity) for item in order.items.all()]),
        'order_date': order.order_date,
        'total_amount': order.total_amount,
        'delivered': order.delivered
        } for order in orders.all()]

    return orders

def get_order(request):
    if request.method == 'POST' and request.POST['getOrder']:
        order = Order.objects.get(id=request.POST['order_id'])
        order = {
            'id': order.id,
            'name': order.name,
            'address': order.address,
            'contact': order.contact,
            'total_amount': order.total_amount,
            'order_date': order.order_date,
            'delivered': order.delivered,
            'items': [{
                'quantity': item.quantity,
                'amount': item.amount,
                'item': item.item.item_name,
                } for item in order.items.all()]
        }
        return JsonResponse({'status': True, 'order': order})


    return JsonResponse({})

def cancel_order(request):
    if request.method == 'POST' and request.POST['cancelOrder']:
        order = Order.objects.get(id=request.POST['order_id'])
        order_id = order.id
        for item in order.items.all():
            order.items.remove(item.id)
            item.delete()
        order.save()
        order.delete()

        return JsonResponse({'status': True, 'order_id': order_id})
    return JsonResponse({})
import json
from django.http import JsonResponse
from Menu.models import Menu
from Order.models import Order, OrderItem

# Create your views here.
def order(request):
    name = request.POST['personName']
    contact = request.POST['phone']
    address = request.POST['location']
    itemName = request.POST['itemName']
    quantity = int(request.POST['quantity'])
    total = request.POST['total']
    item = Menu.objects.get(item_name=itemName)

    orderItem = OrderItem.objects.create(item=item, quantity=quantity, amount=item.price * quantity)

    order = Order.objects.create(name=name, contact=contact, total_amount=total, address=address, user=request.user)
    try:
        order.items.set([orderItem])
        update_order_total(order)
    except Exception as e:
        order.delete()
        # deleting order if any error occurs

    return JsonResponse({"status": True})


def repeat_order(request):
    if request.method == 'POST' and request.POST['order']:
        name = request.POST['personName']
        contact = request.POST['phone']
        address = request.POST['location']

        total = 0
        items = json.loads(request.POST['items'])
        # print(items)
        orderItems = []
        for item in items:
            menuitem = Menu.objects.get(id=item['id'])
            orderItems.append(OrderItem.objects.create(item=menuitem, quantity=int(item['quantity']), amount=menuitem.price * int(item['quantity'])))
            total += orderItems[-1].amount
 
        order = Order.objects.create(name=name, contact=contact, total_amount=total, address=address, user=request.user)
        try:
            order.items.set(orderItems)
            update_order_total(order)
        except Exception as e:
            # deleting order if any error occurs
            order.delete()
            for item in orderItems:
                item.delete()
        
        if request.POST['origin'] == 'checkout':
            # clear the cart
            cart = request.user.cart
            for item in cart.items.all():
                cart.items.remove(item.id)
                item.delete()
            cart.total_amount = 0
            cart.save()

    return JsonResponse({"status": True})


def get_orders(request):
    orders = Order.objects.filter(user=request.user)
    orders = [{
        'id': order.id,
        'items': ", ".join([item.item.item_name + ' x ' + str(item.quantity) for item in order.items.all()]),
        'order_date': order.order_date,
        'total_amount': order.total_amount,
        'status': order.status
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
            'status': order.status,
            'amount': order.total_amount,
            'items': [{
                'quantity': item.quantity,
                'amount': item.amount,
                'name': item.item.item_name,
                'id': item.id,
                'item_id': item.item.id,
                'price': item.item.price,
            } for item in order.items.all()]
        }
        return JsonResponse({'status': True, 'order': order})


    return JsonResponse({})

def cancel_order(request):
    if request.method == 'POST' and request.POST['cancelOrder']:
        order = Order.objects.get(id=request.POST['order_id'])
        order.status = "C"
        order.save()

        return JsonResponse({'status': True, 'order_id': order.id})
    
    return JsonResponse({})

# def repeat_order(request):
#     if request.method == 'POST' and request.POST['repeatOrder']:
#         order = Order.objects.get(id=request.POST['order_id'])
#         # order.status = "C"
#         # order.save()

#         return JsonResponse({'status': True, 'order_id': order.id})
    
#     return JsonResponse({})


def update_order_total(order):
    total = sum([item.quantity * item.item.price for item in order.items.all()])
    order.total = total
    order.save()
    return total
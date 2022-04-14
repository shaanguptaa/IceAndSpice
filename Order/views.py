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
    orders = [{'id': order.id, 'items': [item for item in order.items.all()]} for order in orders.all()]

    return orders
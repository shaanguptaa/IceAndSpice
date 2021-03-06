from django.http import JsonResponse
from django.shortcuts import redirect, render
from Authentication.views import authenticate_user
from Menu.models import Menu
from Order.models import Order, OrderItem
from Order.views import get_orders, update_order_total
from Reservation.models import Reservation
from Reservation.views import get_reservations
from UserProfile.models import Cart, CartItem
from IceAndSpice import get_datetime

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("login")
    context = {
        'user': request.user,
        'orders': get_orders(request),
        'order_count': Order.objects.filter(user=request.user, status="P").count(),
        'reservations_count': Reservation.objects.filter(user=request.user, date_of_reservation__gt=get_datetime()).count(),
        'cart_count': request.user.cart.items.all().count(),
        'cart': get_cart(request),
        'reservations': get_reservations(request),
    }

    return render(request, "UserProfile/index.html", context=context)

def update_profile(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address'].strip()

        user = authenticate_user(username=username, password=password)
        if user is not None:
            updated_items = []
            if username != request.user.username:
                request.user.username = username
                request.user.save()
                updated_items.append('username')
            if fname != request.user.first_name:
                request.user.first_name = fname
                request.user.save()
                updated_items.append('fname')
            if lname != request.user.last_name:
                request.user.last_name = lname
                request.user.save()
                updated_items.append('lname')
            if email != request.user.email:
                request.user.email = email
                request.user.save()
                updated_items.append('email')
            if phone != request.user.profile.phone:
                request.user.profile.phone = phone
                request.user.profile.save()
                updated_items.append('phone')
            if address != request.user.profile.address:
                request.user.profile.address = address
                request.user.profile.save()
                updated_items.append('address')

            if len(updated_items) > 0:
                return JsonResponse({'status': True})
        else:
            return JsonResponse({'status': False, 'msg': 'Incorrect Password'})

    return JsonResponse({'status': False, "msg": ''})

def change_item_quantity(request):
    if request.method == "POST" and request.POST['changeQuantity']:
        item = request.POST['item']
        item = request.user.cart.items.all().get(id=item)
        q = int(request.POST['changeBy'])
        if q == 1:
            item.quantity += 1
        elif q == -1 and item.quantity > 1:
            item.quantity -= 1
        else:
            item.quantity = 1
        item.amount = item.quantity * item.item.price
        item.save()
        total = update_cart_total(request.user.cart)

        return JsonResponse({'status': True, 'quantity': item.quantity, 'price': item.item.price, 'amount': item.amount, 'total': total})

    return JsonResponse({})

def update_cart_total(cart):
    total = sum([item.quantity * item.item.price for item in cart.items.all()])
    cart.total_amount = total
    cart.save()
    return total

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

    total = update_cart_total(cart)

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

    num_items = cart.items.all().count()

    total = update_cart_total(cart)


    return JsonResponse({'status': True, 'total': total, 'num_items': num_items})

def get_cart_for_homepage(user):
    cart = Cart.objects.get(user=user)
    data = [item.item.id for item in cart.items.all()]
    return data

def checkout(request):
    if request.method == 'POST' and request.POST['checkout']:
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['addres']
        
        items = request.POST['items']
        # structure for post items
        # items = [{'id': id, 'price': price, 'quantity': quantity}] array of dict

        orderItems = [OrderItem.objects.create(item=Menu.objects.get(id=item.id), quantity=item.quantity, amount=item.price) for item in items]
        order = Order.objects.create(name=name, email=email, contact=phone, address=address, user=request.user)

        order.items.set(orderItems)

        update_order_total(order)

        return JsonResponse({'status': True})

    return JsonResponse({})

def getCartAjax(request):
    if request.method == "POST" and request.POST['get_details']:
        cart = Cart.objects.get(user=request.user)
        cart = {
            'total_amount': cart.total_amount,
            'items': [{
                'quantity': item.quantity,
                'amount': item.amount,
                'name': item.item.item_name,
                'id': item.id,
                'item_id': item.item.id,
                'price': item.item.price,
            } for item in cart.items.all()]
        }


    return JsonResponse({'status': True, 'cart': cart})


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
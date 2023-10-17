from datetime import date, datetime, timedelta
from json import loads
import os
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from Menu.models import Menu

from Menu.views import get_all_items, getmenu
from Order.models import Order
from Order.views import get_all_orders
from Reservation.models import Reservation
from Reservation.views import get_all_reservations
# from administrator.forms import ImageForm
from administrator.models import Feedback, Offer

# Create your views here.
def index(request):

    if request.user.is_anonymous or not request.user.is_superuser:
        return redirect("homepage")

    context = {
        'menu': get_all_items(),
        'feedbacks': get_feedbacks(),
        'reservations': get_all_reservations(),
        'orders': get_all_orders(),
        'offers': get_offers(),
        'menu_items': getmenu(),
        # 'form': ImageForm(),
    }
    return render(request, "administrator/index.html", context)

# def handle_admin_signup(request):
#     if request.method == 'POST' and request.POST['signup-btn']:
#         username = request.POST['username']
#         password = request.POST['password']

#         user = User.objects.create_user(username=username, password=password)
#         user.save()
#         return redirect("administrator_index")
#     else:
#         return render(request, "administrator/signup.html")


def handle_admin_login(request):
    if request.method == 'POST' and request.POST['login-btn']:
        username = request.POST['username'] 
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("administrator_index") if user.is_superuser else redirect("homepage")
        else:
            return redirect("login")
    else:
        return redirect("login")

def handle_admin_logout(request):
    logout(request)
    return redirect("login")

def get_feedbacks():
    feedbacks = [{
        'name': feedback.name,
        'email': feedback.email,
        'message': feedback.message,
        'feedback_date': feedback.feedback_date,
    } for feedback in Feedback.objects.all().order_by('-feedback_date')]
    
    return feedbacks

def update_profile(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']

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
        
        if len(updated_items) > 0:
            return JsonResponse({'status': True})

    return JsonResponse({})

def get_counts(request):
    
    orders_delivered = Order.objects.filter(status="D", delivery_date__gte=date.today()).count()
    orders_pending = Order.objects.filter(status="P", order_date__gte=date.today()).count()

    reservations_confirmed = Reservation.objects.filter(status="R", date_of_reservation__gte=date.today(), date_of_reservation__lte=date.today() + timedelta(days=1)).count()
    tables_booked = Reservation.objects.filter(date_booked__gte=date.today()).count()

    return JsonResponse({
        'status': True,
        'orders_delivered': orders_delivered,
        'orders_pending': orders_pending,
        'reservations_confirmed': reservations_confirmed,
        'tables_booked': tables_booked,
    })


def get_offers(expired=True):
    if expired:
        offers = Offer.objects.all()
    else:
        offers = Offer.objects.filter(expiry_date__gte=date.today())

    return [{
        'title': offer.title,
        'desc': offer.desc,
        'discount_percent': offer.discount_percent,
        'coupon_code': offer.coupon_code,
        'expiry_date': offer.expiry_date,
        'is_expired': True if offer.expiry_date < date.today() else False,
        'items': ', '.join([item.item_name for item in offer.items.all()]),
        'image': offer.image.url,
    } for offer in offers.all()]

def get_offer(request):
    if request.method == 'POST' and request.POST['get_offer']:
        offer = Offer.objects.get(coupon_code=request.POST['id'])
        # image = offer.image
        offer = {
            'title': offer.title,
            'desc': offer.desc,
            'discount_percent': offer.discount_percent,
            'coupon_code': offer.coupon_code,
            'expiry_date': offer.expiry_date,
            'is_expired': True if offer.expiry_date < date.today() else False,
            'items': [item.id for item in offer.items.all()],
            'image': offer.image.url,
        }
        return JsonResponse({'status': True, 'offer': offer})

    return JsonResponse({'status': False})

def update_offer(request):
    if request.method == 'POST' and request.POST['update_offer']:
        offer = Offer.objects.get(coupon_code=request.POST['prev_code'])
        # form = ImageForm(request.POST, request.FILES, instance=offer)
        # if form.is_valid():
        #     imagePath = form.instance.image.url
        #     # newImage = form.fields['image']
        #     print(form.data)
        #     if os.path.exists(imagePath):
        #         os.remove(imagePath)
        #     form.save()
        
        offer.coupon_code = request.POST['new_code'].upper()
        offer.title = request.POST['title']
        offer.desc = request.POST['desc']
        offer.expiry_date = datetime.strptime(request.POST['expiry_date'], "%Y-%m-%d").date()
        offer.discount_percent = request.POST['discount']
        offer.save()
        offer.items.set(loads(request.POST['items']))
        
        offer = {
            'title': offer.title,
            'desc': offer.desc,
            'discount_percent': offer.discount_percent,
            'coupon_code': offer.coupon_code,
            'expiry_date': offer.expiry_date.strftime("%B %d, %Y"),
            'is_expired': True if offer.expiry_date < date.today() else False,
            'items': ', '.join([item.item_name for item in offer.items.all()]),
            'image': offer.image.url,
        }

        if request.POST['new_code'] != request.POST['prev_code']:
            Offer.objects.get(coupon_code=request.POST['prev_code']).delete()

        return JsonResponse({'status': True, 'offer': offer})

    return JsonResponse({'status': False})

def add_offer(request):
    if request.method == 'POST' and request.POST['add_offer']:
        # form = ImageForm(request.POST, request.FILES, instance=offer)
        # if form.is_valid():
        #     imagePath = form.instance.image.url
        #     # newImage = form.fields['image']
        #     print(form.data)
        #     if os.path.exists(imagePath):
        #         os.remove(imagePath)
        #     form.save()
        
        coupon_code = request.POST['code'].upper()
        title = request.POST['title']
        desc = request.POST['desc']
        expiry_date = datetime.strptime(request.POST['expiry_date'], "%Y-%m-%d").date()
        discount_percent = request.POST['discount']
        
        offer = Offer.objects.create(coupon_code=coupon_code, title=title, desc=desc, expiry_date=expiry_date, discount_percent=discount_percent)
        offer.items.set(loads(request.POST['items']))


        offer = {
            'title': offer.title,
            'desc': offer.desc,
            'discount_percent': offer.discount_percent,
            'coupon_code': offer.coupon_code,
            'expiry_date': offer.expiry_date.strftime("%B %d, %Y"),
            'is_expired': True if offer.expiry_date < date.today() else False,
            'items': ', '.join([item.item_name for item in offer.items.all()]),
            'image': offer.image.url,
        }

        return JsonResponse({'status': True, 'offer': offer})

    return JsonResponse({'status': False})

def delete_offer(request):
    if request.method == 'POST' and request.POST['delete_offer']:
        Offer.objects.get(coupon_code=request.POST['coupon_code']).delete()

        return JsonResponse({'status': True, 'code': request.POST['coupon_code']})

    return JsonResponse({'status': False})

def check_coupon(request):
    if request.method == 'POST' and request.POST['check_coupon']:
        msg = "Invalid Coupon Code"
        try:
            offer = Offer.objects.get(coupon_code=request.POST['coupon_code'].upper())
            item = Menu.objects.get(item_name=request.POST['itemName'])
            if (offer.expiry_date >= date.today()) and (item not in offer.items.all()):
                msg = "Coupon Unavailable"
                raise Exception
            offer = {
                'code': offer.coupon_code,
                'discount': offer.discount_percent,
            }
            return JsonResponse({'status': True, 'offer': offer})
        except Exception as e:
            return JsonResponse({'status': False, 'msg': msg})

    return JsonResponse({'status': False})


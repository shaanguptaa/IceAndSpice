from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from Menu.views import get_all_items
from Order.views import get_all_orders
from Reservation.views import get_all_reservations
from administrator.models import Feedback

# Create your views here.
def index(request):

    if request.user.is_anonymous or not request.user.is_superuser:
        return redirect("homepage")

    context = {
        'menu': get_all_items(),
        'feedbacks': get_feedbacks(),
        'reservations': get_all_reservations(),
        'orders': get_all_orders(),
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
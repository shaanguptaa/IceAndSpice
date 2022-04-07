from django.http import HttpResponse
from django.shortcuts import render
from Menu import views as menu

# Create your views here.
def index(request):
    # if request.user.username == 'admin':
    #     return HttpResponse('<h4>You are logged in as: ' + request.user.username + '</h4> <br>Login to another account to continue')
    context = {
        'menu': menu.getmenu(),
        'cartItems': menu.get_cart(request.user) if not request.user.is_anonymous else None,
    }

    # print(context['cartItems']['quantity']['O-8769'])
    # temp = menu.order_items(request.user)
    return render(request, 'IceAndSpice/index.html', context=context)

def temp(request):
    return render(request, 'IceAndSpice/temp.html', context=menu.getmenu())
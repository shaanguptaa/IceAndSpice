from django.http import JsonResponse
from Menu.models import Menu

# Create your views here.
def getmenu():
    return {
        'main': [item for item in Menu.objects.filter(category='Main').values()] or None,
        'drinks': [x for x in Menu.objects.filter(category='Drinks').values()] or None,
        'desserts': [x for x in Menu.objects.filter(category='Desserts').values()] or None,
    }


def get_all_items():
    return [item for item in Menu.objects.all().order_by('-category')]


def get_item(request):
    if request.method == 'POST' and request.POST['get_item']:
        item = Menu.objects.get(id=request.POST['item_id'])
        item = {
            'id': item.id,
            'item_name': item.item_name,
            'category': item.category,
            'status': item.status,
            'price': item.price,
        }
        return JsonResponse({'status': True, 'item': item})

    return JsonResponse({'status': False})


def update_item(request):
    if request.method == 'POST' and request.POST['update_item']:
        item = Menu.objects.get(id=request.POST['id'])
        item.name = request.POST['name']
        item.category = request.POST['category']
        item.status = request.POST['status']
        item.price = request.POST['price']
        item.save()
        item = {
            'id': item.id,
            'item_name': item.item_name,
            'category': item.category,
            'status': item.status,
            'price': item.price,
        }
        return JsonResponse({'status': True, 'item': item})

    return JsonResponse({'status': False})

def delete_item(request):
    if request.method == 'POST' and request.POST['delete_item']:
        item = Menu.objects.get(id=request.POST['id'])
        item.delete()
        return JsonResponse({'status':True, 'item_id': request.POST['id']})

    return JsonResponse({'status': False})

def add_item(request):
    if request.method == 'POST' and request.POST['add_item']:
        name = request.POST['name']
        category = request.POST['category']
        status = request.POST['status']
        price = request.POST['price']
        item = Menu.objects.create(item_name=name, item_desc=name, category=category, status=status, price=price)
        item = {
            'id': item.id,
            'item_name': item.item_name,
            'category': item.category,
            'status': item.status,
            'price': item.price,
        }
        return JsonResponse({'status': True, 'item': item})

    return JsonResponse({'status': False})
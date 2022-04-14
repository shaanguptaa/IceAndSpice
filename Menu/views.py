from Menu.models import Menu

# Create your views here.
def getmenu():
    return {
        'main': [item for item in Menu.objects.filter(category='Main').values()] or None,
        'drinks': [x for x in Menu.objects.filter(category='Drinks').values()] or None,
        'desserts': [x for x in Menu.objects.filter(category='Desserts').values()] or None,
    }

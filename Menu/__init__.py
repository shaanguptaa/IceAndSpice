import random

def generate_order_id():
    return 'O-' + str(random.randint(1000, 9999))

def generate_menu_id():
    return 'M-' + str(random.randint(1000, 9999))
import random

def generate_order_id():
    return 'O-' + str(random.randint(1000, 9999))
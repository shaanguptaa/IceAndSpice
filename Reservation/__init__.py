import random

def generate_reservation_id():
    return 'R-' + str(random.randint(1000, 9999))
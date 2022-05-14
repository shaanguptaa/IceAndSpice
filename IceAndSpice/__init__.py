from datetime import datetime

def get_datetime():
    return datetime.now()

def get_date():
    return get_datetime().date()

import random

def get_offer_image():
    return 'offers/default' + str(random.randint(1, 5)) + '.jpg'
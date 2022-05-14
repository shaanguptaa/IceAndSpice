import random

def get_offer_image():
    return 'offers/default' + str(random.randint(1, 5)) + '.jpg'
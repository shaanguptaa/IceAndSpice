from datetime import datetime

def get_datetime():
    return datetime.now()

def get_date():
    return get_datetime().date()

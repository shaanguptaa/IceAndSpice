from django.http import JsonResponse
from Reservation.models import Reservation
from datetime import datetime, timedelta
from pytz import UTC

# Create your views here.
def reserve_table(request):
    if not request.user.is_authenticated:
        return JsonResponse({})
    if request.method == 'POST' and request.POST['reserve']:
        try:
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            date = request.POST['date']
            time = request.POST['time']
            persons = request.POST['persons']

            dor = [int(x) for x in date.split('-')]
            dor.extend([int(x) for x in time.split(':')])

            dor = datetime(dor[0], dor[1], dor[2], dor[3], dor[4])

            Reservation.objects.create(name=name, email=email, phone=phone, date_of_reservation=dor, persons=persons, user=request.user)

            return JsonResponse({'status': 'Success', 'persons': persons, 'date': date, 'time': time})

        except Exception as e:
            return JsonResponse({'status': 'Failed', 'error': e})

    return JsonResponse({})

def get_reservations(request):
    if not request.user.is_authenticated:
        reservations = None
    else:
        reservations = Reservation.objects.filter(user=request.user).order_by('-date_booked')
        # print(reservations)
        # reservations - [{
        #     'id': reservation.id,
        #     'reserve_date': reservation.date_of_reservation.date(),
        #     'reserve_time': reservation.date_of_reservation.time(),
        #     'booked': reservation.date_booked,
        #     'persons': reservation.persons,
        #     'status': reservation.status,
        # } for reservation in reservations]

    return reservations

def get_all_reservations():
    reservations = Reservation.objects.all().order_by('-date_booked')
    return reservations

def get_reservation_details(request):
    if request.method == 'POST' and request.POST['get_details']:
        id = request.POST['reservation_id']
        reservation = Reservation.objects.get(id=id)
        # print(reservation.date_booked + , '\n', reservation.date_of_reservation)
        reservation = {
            'id': reservation.id,
            'name': reservation.name,
            'email': reservation.email,
            'phone': reservation.phone,
            'date_booked': reservation.date_booked + timedelta(hours=5, minutes=30),
            'date_of_reservation': reservation.date_of_reservation + timedelta(hours=5, minutes=30),
            'persons': reservation.persons,
            'status': reservation.status,
        }

        return JsonResponse({'status': True, 'reservation': reservation})
    
    return JsonResponse({'status': False})

def cancel_reservation(request):
    if request.method == 'POST' and request.POST['cancel_reservation']:
        reservation = Reservation.objects.get(id=request.POST['reservation_id'])
        if UTC.localize(datetime.now()) + timedelta(hours=1) <= reservation.date_of_reservation + timedelta(hours=5, minutes=30):
            reservation.status = "C"
            reservation.save()

            return JsonResponse({'status': True, 'reservation_id': reservation.id})
        else:
            return JsonResponse({'status': False})
    return JsonResponse({'status': False})

def confirm_reservation(request):
    if request.method == 'POST' and request.POST['confirm_reservation']:
        reservation = Reservation.objects.get(id=request.POST['reservation_id'])
        reservation.status = "R"
        reservation.save()

        return JsonResponse({'status': True, 'reservation_id': reservation.id})
    return JsonResponse({'status': False})
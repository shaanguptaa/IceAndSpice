from django.http import JsonResponse
from django.shortcuts import render
from Reservation.models import Reservation
from datetime import datetime

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
        reservations, status = None, False
    else:
        reservations = Reservation.objects.filter(user=request.user)
        print(reservations)

        reservations = [x for x in reservations.values()] or None
        status = True

    return JsonResponse({'reservations': reservations, 'status': status})
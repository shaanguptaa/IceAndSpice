# from random import randint
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

from Reservation import generate_reservation_id

# Create your models here.
class Reservation(models.Model):
    id = models.CharField(max_length=6, default=generate_reservation_id, primary_key=True, editable=False)
    name = models.CharField(max_length=20, default="")
    email = models.EmailField(max_length=50, default="")
    phone = models.CharField(max_length=10, default="")
    date_booked = models.DateTimeField(default=datetime.now())
    date_of_reservation = models.DateTimeField(default=datetime.now())
    persons = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Booking ' + str(self.id)

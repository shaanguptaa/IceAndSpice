from django.db import models
from django.contrib.auth.models import User
from Reservation import generate_reservation_id
from IceAndSpice import get_datetime

# Create your models here.
class Reservation(models.Model):
    id = models.CharField(max_length=6, default=generate_reservation_id, primary_key=True, editable=False)
    name = models.CharField(max_length=20, default="")
    email = models.EmailField(max_length=50, default="")
    phone = models.CharField(max_length=10, default="")
    date_booked = models.DateTimeField(default=get_datetime)
    date_of_reservation = models.DateTimeField(default=get_datetime)
    persons = models.IntegerField(default=1)
    status = models.CharField(max_length=1, choices=[("R", "Reserved"), ("P", "Pending"), ('C', 'Cancelled')], default="P")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Booking ' + str(self.id)

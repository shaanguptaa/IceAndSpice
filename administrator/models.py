from django.db import models
from django.contrib.auth.models import User

from IceAndSpice import get_date, get_datetime, get_offer_image
from Menu.models import Menu

# Create your models here.
class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, default="")
    email = models.EmailField(max_length=50, default="")
    message = models.TextField(default="")
    feedback_date = models.DateTimeField(default=get_datetime)

    def __str__(self):
        return self.name + ' - ' + self.message[:10] + ' ...'


class Offer(models.Model):
    title = models.CharField(max_length=20, default="")
    desc = models.TextField(default="")
    coupon_code = models.CharField(primary_key=True,max_length=10, default="")
    discount_percent = models.PositiveIntegerField(default=0)
    expiry_date = models.DateField(default=get_date)
    items = models.ManyToManyField(Menu, blank=True)
    image = models.ImageField(upload_to='offers/', default=get_offer_image)

    def __str__(self):
        return self.title + ' : ' + str(self.discount_percent) + '%' + ' discount'
    


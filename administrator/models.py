from django.db import models
from django.contrib.auth.models import User

from IceAndSpice import get_datetime

# Create your models here.
class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, default="")
    email = models.EmailField(max_length=50, default="")
    message = models.TextField(default="")
    feedback_date = models.DateTimeField(default=get_datetime)

    def __str__(self):
        return self.name + ' - ' + self.message[:10] + ' ...'

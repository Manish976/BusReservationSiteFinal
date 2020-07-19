from datetime import datetime, date, time

from django.contrib.auth.models import User
from django.db import models


class Bus_description(models.Model):
    BusName   = models.CharField(max_length=20,default="Lamjhung Travels")
    BusNumber = models.CharField(max_length=10)
    BusType   = models.CharField(max_length=30)
    From      = models.CharField(max_length=40)
    To        = models.CharField(max_length=40)
    Shift     = models.CharField(max_length=10)
    status    = models.BooleanField(default=False)
    images    = models.ImageField(upload_to='pics')
    dates     = models.DateField(default=date.today())
    pick_time = models.TimeField(default=datetime.now().time())
    pick_destination= models.CharField(max_length=30,default="Gongabu Bus Park")
    fare      = models.IntegerField(default=100)

class Seats(models.Model):
    seat_number = models.CharField(max_length=5)


class reservation(models.Model):
    bus_description = models.ForeignKey(Bus_description, default=None, on_delete=models.CASCADE)
    seat            = models.ForeignKey(Seats, default=None, on_delete=models.CASCADE)
    user            = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    date            = models.DateField(default=datetime.today())





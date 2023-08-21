from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Car(models.Model):
    plate_number=models.CharField(max_length=10)
    brand=models.CharField(max_length=100)
    model=models.CharField(max_length=30)
    year=models.SmallIntegerField(max_length=30)
    gear=models.CharField(max_length=30)
    rent_per_day=models.IntegerField()
    availability=models.BooleanField()

def __str__(self):
        return f"{self.plate_number} - {self.brand}- {self.model}"


class Reservation(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    car=models.ForeignKey(Car,on_delete=models.CASCADE,related_name="reservations")
    start_date=models.DateTimeField(auto_now_add=True)
    end_date=models.DateTimeField()
    def __str__(self):
        return f"{self.user} - {self.car}"
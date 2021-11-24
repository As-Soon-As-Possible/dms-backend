from django.db import models
from datetime import datetime

class Victim(models.Model):
    name = models.CharField(max_length=30)
    mobile_no = models.CharField(max_length=15, primary_key=True)
    location = models.CharField(max_length=30)
    latitude = models.DecimalField(max_digits=19, decimal_places=16)
    longitude = models.DecimalField(max_digits=19, decimal_places=16)
    date_created = models.DateTimeField(default=datetime.now())
    additional_info = models.CharField(max_length=1000)

    def __str__(self):
        return self.name + ' - ' + self.mobile_no

class Volunteer(models.Model):
    name = models.CharField(max_length=30)
    mobile_no = models.CharField(max_length=15, primary_key=True)
    gender = models.CharField(max_length=15)
    age = models.IntegerField()
    qualification = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ' - ' + self.qualification

class Camp(models.Model):
    location = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    latitude = models.DecimalField(max_digits=19, decimal_places=16)
    longitude = models.DecimalField(max_digits=19, decimal_places=16)
    max_capacity = models.IntegerField()
    def __str__(self):
        return self.location + ' - ' + self.max_capacity

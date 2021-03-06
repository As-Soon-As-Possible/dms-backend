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
    qualification = models.CharField(max_length=100, null=True )
    location = models.CharField(max_length=30, null=True)
    latitude = models.DecimalField(max_digits=19, decimal_places=16, null=True, default=0)
    longitude = models.DecimalField(max_digits=19, decimal_places=16,null=True, default=0)

    def __str__(self):
        return self.name + ' - ' + self.mobile_no

class Camp(models.Model):
    name = models.CharField(max_length=30, default="aaaa")
    location = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    latitude = models.DecimalField(max_digits=19, decimal_places=16)
    longitude = models.DecimalField(max_digits=19, decimal_places=16)
    max_capacity = models.IntegerField()
    available_slots = models.IntegerField(default=5)
    def __str__(self):
        return self.location + ' - ' + str(self.max_capacity)

class Assigned(models.Model):
    assigned_victim = models.ForeignKey(Victim,  on_delete=models.CASCADE, unique=True)
    assigned_volunteer = models.ForeignKey(Volunteer,  on_delete=models.CASCADE)

    class Meta:
        unique_together = (('assigned_victim', 'assigned_volunteer'))
        index_together = (('assigned_victim', 'assigned_volunteer'))

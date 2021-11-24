from django.contrib import admin
from .models import Victim,Volunteer, Assigned
# Register your models here.
admin.site.register(Victim)
admin.site.register(Volunteer)
admin.site.register(Assigned)

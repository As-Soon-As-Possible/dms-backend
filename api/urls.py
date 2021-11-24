from django.urls import path, include
from .views import UserRecordView, GetRescueMapAPI,VictimSMSAPI,VolunteerRecordView, FindVictim,FindCamp
from django.conf.urls import url, include
from django.contrib import admin

app_name = 'api'
urlpatterns = [
    path('user/', UserRecordView.as_view(), name='users'),
    path('rescuemap/', GetRescueMapAPI.as_view(), name='rescuemap'),
    path('victimcreate/',VictimSMSAPI.as_view(),name='victimcreate'),
    path('volunteer/', VolunteerRecordView.as_view(), name='volunteer'),
    path('findvictim/', FindVictim.as_view(), name='findVictim'),
    path('findcamp/', FindCamp.as_view(), name='findCamp')
]

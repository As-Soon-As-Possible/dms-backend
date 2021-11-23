from django.urls import path
from .views import UserRecordView
from django.conf.urls import url, include
from django.contrib import admin

app_name = 'api'
urlpatterns = [
    path('user/', UserRecordView.as_view(), name='users'),
]

from django.urls import path
from .views import bmi

urlpatterns = [
    path('', bmi),
]
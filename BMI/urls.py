from django.urls import path
from BMI.views import Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
]

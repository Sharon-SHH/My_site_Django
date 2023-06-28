from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('<int:month>', views.monthly_digits),
    path('<str:month>', views.index, name="month-direct"),
    
]

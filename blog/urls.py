from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<slug:slug>', views.details, name="blog-detail") 
    # path('<int:id>', views.details, name="blog-detail") 
    #path('<str:title>', views.details) 
]

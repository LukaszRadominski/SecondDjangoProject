from django.urls import path
from . import views

urlpatterns = [
    path('', views.carslist, name = 'carslist') 
]
# we define the urlpatterns for this module.
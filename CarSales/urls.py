from django.urls import path
from . import views

urlpatterns = [
    path('', views.carslist, name = 'carslist'), 
    path('addcar', views.addcar, name = 'addcar')
]
# we define the urlpatterns for this module.
# Add a new url pattern for addcar in the app urls.py. 
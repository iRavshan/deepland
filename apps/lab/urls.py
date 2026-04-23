from django.urls import path
from . import views

app_name = 'lab'

urlpatterns = [
    path('computer-network/', views.computer_network, name='computer_network'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='lab'),
    path('computer-network/', views.computer_network, name='computer_network'),
    path('logic-circuit/', views.logic_circuit, name='logic_circuit'),
]

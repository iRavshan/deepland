from django.urls import path
from . import views

app_name = 'lab'

urlpatterns = [
    path('', views.index, name='index'),
    path('computer-network/', views.computer_network, name='computer_network'),
    path('logic-circuit/', views.logic_circuit, name='logic_circuit'),
]

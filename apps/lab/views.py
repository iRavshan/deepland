from django.shortcuts import render

def index(request):
    return render(request, 'lab/index.html')

def computer_network(request):
    return render(request, 'lab/computer_network.html')

def logic_circuit(request):
    return render(request, 'lab/logic_circuit.html')
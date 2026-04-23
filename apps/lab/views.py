from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def computer_network(request):
    return render(request, 'lab/computer_network.html')

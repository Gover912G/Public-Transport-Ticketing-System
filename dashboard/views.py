from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'dash/dash.html', {'nav':'dash'})


    
@login_required
def Tickets(request):
    return render(request, 'dash/Tickets.html', {'nav':'tickets'})


def scan_ticket(request):
    
    return render(request, 'dash/scan_ticket.html', {'nav':'tick'})
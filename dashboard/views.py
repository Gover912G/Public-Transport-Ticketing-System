from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'dash/dash.html', {'nav':'dash'})

def Tickets(request):
    return render(request, 'dash/Tickets.html', {'nav':'tickets'})
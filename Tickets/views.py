import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from.models import Ticket
from .forms import UpdateTicketForm, TicketForm



# Create your views here.


def ticket_details(request, pk):
    ticket = Ticket.objects.get(pk=pk)

    
    context = {'ticket':ticket}

    return render(request, './main/mytickets.html', context)


# booking a ticket
def book_ticket(request):
    if request.method =='POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.created_by = request.user
            var.ticket_status = 'Pending'
            var.save()

            messages.info(request, 'Ticket booked successfully.')
            return redirect('home')
        else:
            messages.warning(request, 'Something went wrong')
            return redirect('bookTicket')
        
    else:
        form = TicketForm()
        context = {
            'nav':'tickets',
            'form':form
            }
        return render(request, './main/Ticket_booking.html', context)
    

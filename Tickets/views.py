import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from.models import Ticket
from .forms import UpdateTicketForm, TicketForm



# Create your views here.

@login_required
def ticket_details(request, pk):
    ticket = Ticket.objects.get(pk=pk)

    
    context = {'ticket':ticket}

    return render(request, './main/mytickets.html', context)


@login_required
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
            return redirect('mytickets')
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
    




@login_required
# booking a ticket
def update_ticket(request, pk):
    ticket = Ticket.objects.get(pl=pk)
    if request.method =='POST':
        form = UpdateTicketForm(request.POST, instance = ticket)
        if form.is_valid():
            form.save()

            messages.info(request, 'Ticket updated successfully.')
            return redirect('mytickets')
        else:
            messages.warning(request, 'Something went wrong')
            # return redirect('bookTicket')
        
    else:
        form = UpdateTicketForm(instance=ticket)
        context = {
            'nav':'tickets',
            'form':form
            }
        return render(request, './main/Ticket_updating.html', context)
    
#view all createdtickets

def All_tickets(request):
    ticks = Ticket.objects.filter(created_by=request.user)
    context = {'ticks':ticks}

    return render(request, './dash/Tickets.html', context)




def Booked_tickets(request):
    tickets = Ticket.objects.filter(ticket_status=Pending)
    context = {'tickets':'tickets'}

    return render(request, 'dash/booked_tickets.html', context)


def Accept_ticket(request,pk):
    ticket = Ticket.objects.get(pk=pk)
    ticket.created_by = request.user
    ticket.ticket_status = 'Active'
    ticket.accepted_date = datetime.datetime.now()
    ticket.save()
    

    messages.info(request, 'Ticket accepted, enjoy the ride')
    return redirect('dashboard')




def Close_ticket(request,pk):
    ticket = Ticket.objects.get(pk=pk)
    ticket.ticket_status = 'Completed'
    ticket.is_resolved = True
    ticket.accepted_date = datetime.datetime.now()
    ticket.save()
    

    messages.info(request, 'Ticket Resolved, Thank you for choosing us')
    return redirect('dashboard')

def workspace(request):
    tickets = Ticket.objects.filter(created_by=request.user, is_resolved=False)
    context = {'tickets':'tickets'}

    return render(request, 'workspace.html', context)


def All_closed_tickets(request):
    tickets = Ticket.objects.filter(created_by= request.user, is_resolved=True)
    context = {'tickets':'tickets'}
    return render(request, 'closed_tickets.html', context)
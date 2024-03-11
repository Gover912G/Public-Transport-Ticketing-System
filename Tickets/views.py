from django.utils import timezone
import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from.models import Ticket
from .forms import UpdateTicketForm, TicketForm
from Users.models import User
from .models import Ticket


from rest_framework import viewsets
from .serializers import TicketSerializer
from .models import Ticket

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

# Create your views here.

@login_required
def ticket_details(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    t = User.objects.get(username=ticket.created_by)
    tickets_per_user = t.created_by.all()

    
    context = {'ticket':ticket, 'tickets_per_user': tickets_per_user}

    return render(request, './main/tickets_details.html', context)



@login_required
def my_tickets(request):
    tickets = Ticket.objects.filter(created_by=request.user)
    context = {'tickets': tickets}
    return render(request, './main/tickets_details.html', context)

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
            print("Form is valid")

            messages.info(request, 'Ticket booked successfully.')
            return redirect('tickets:mytickets')
        else:
            print("Form is not valid")
            print(form.errors)
            messages.warning(request, 'Something went wrong')
            return redirect('main:home')
        
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
    ticket = Ticket.objects.get(pk=pk)
    if not ticket.is_resolved:
        if request.method =='POST':
            form = UpdateTicketForm(request.POST, instance = ticket)
            if form.is_valid():
                form.save()

                messages.info(request, 'Ticket updated successfully.')
                return redirect('tickets:mytickets')
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
    else:
        messages.warning(request, "Ticket cannot be changed")
        return redirect('main:home')
    
#view all createdtickets

def All_tickets(request):
    tickets = Ticket.objects.filter(created_by=request.user).order_by('-date_created')
    context = {'tickets':tickets}

    return render(request, './main/all_tickets.html', context)



# All Tickets that have been booked by customers to be viewed by admin
def Booked_tickets(request):
    tickets = Ticket.objects.filter(ticket_status='Pending')
    context = {'tickets':tickets}

    return render(request, './dash/booked_tickets.html', context)

# view for accepting the ticket(scan)
def Accept_ticket(request,pk):
    ticket = Ticket.objects.get(pk=pk)
    ticket.accepted_by = request.user
    ticket.ticket_status = 'Active'
    ticket.accepted_date = datetime.datetime.now()
    ticket.save()
    

    messages.info(request, 'Ticket accepted,')
    return redirect('tickets:workspace')


def scan_ticket(request):
    if request.method == 'POST':
        scanned_code = request.POST.get('scanned_code')
        try:
            ticket = Ticket.objects.get(ticket_number=scanned_code)
            if ticket.ticket_status == 'Pending':
                ticket.accepted_by = request.user
                ticket.ticket_status = 'Active'
                ticket.accepted_date = datetime.datetime.now()
                ticket.save()
                messages.success(request, 'Ticket accepted')
                return redirect('tickets:workspace')
            else:
                messages.error(request, 'Ticket has already been accepted or completed')
        except Ticket.DoesNotExist:
            messages.error(request, 'Ticket not found')

    return render(request, 'dash/scan_ticket.html')


def Close_ticket(request,pk):
    ticket = Ticket.objects.get(pk=pk)
    ticket.ticket_status = 'Completed'
    ticket.is_resolved = True
    ticket.accepted_date = datetime.datetime.now()
    ticket.save()
    

    messages.info(request, 'Ticket Resolved, Thank you for choosing us')
    return redirect('dashboard')

# tickets that a conductor has received but not yet resolved
def workspace(request):
    tickets = Ticket.objects.filter(accepted_by=request.user, is_resolved=False)
    context = {'tickets':tickets}

    return render(request, 'dash/workspace.html', context)

# tickets that a conductor has received and are resolved

def All_closed_tickets(request):
    tickets = Ticket.objects.filter(created_by= request.user, is_resolved=True)
    context = {'tickets':'tickets'}
    return render(request, 'dash/closed_tickets.html', context)
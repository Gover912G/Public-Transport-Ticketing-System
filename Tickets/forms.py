from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['route', 'start_point', 'stop_point','phone_number']


class UpdateTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['route', 'start_point', 'stop_point','phone_number']

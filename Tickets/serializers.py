from rest_framework import serializers
from .models import Route, Stage, Ticket



class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
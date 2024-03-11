import uuid
from django.db import models
from Users.models import User
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

from rest_framework import serializers, viewsets

class Stage(models.Model):
    stage_name = models.CharField(max_length=100)

    def __str__(self):
        return self.stage_name

class Route(models.Model):
    route_number = models.IntegerField(blank=False)
    route_name = models.CharField(blank=False, max_length=100)
    stage = models.ManyToManyField(Stage)

    def __str__(self):
        return self.route_name

class Ticket(models.Model):
    status_choices = (
        ('Active', 'Active'),
        ('Completed', 'Completed'),
        ('Pending', 'Pending')
    )
    ticket_number = models.UUIDField(default=uuid.uuid4)
    route = models.ForeignKey(Route, related_name='route', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by')
    date_created = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)
    accepted_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    accepted_date = models.DateTimeField(null=True, blank=True)
    closed_date = models.DateTimeField(null=True, blank=True)
    ticket_status = models.CharField(max_length=20, choices=status_choices)
    start_point = models.ForeignKey(Stage, related_name='start_point', on_delete=models.CASCADE)
    stop_point = models.ForeignKey(Stage, related_name='stop_point', on_delete=models.CASCADE)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)

    def __str__(self):
        return str(self.route)

    def save(self, *args, **kwargs):
        from .serializers import TicketSerializer  # Import inside the method
        qr = qrcode.QRCode(
            version=1,
            box_size=4,
            border=5
        )
        data = f'Ticket Number: {self.ticket_number}\nRoute: {self.route.route_name}\nCreated by: {self.created_by.username}\nStart point: {self.start_point}\nStop point: {self.stop_point}'
        
        serializer = TicketSerializer(instance=self)
        serialized_data = serializer.data
        for key, value in serialized_data.items():
            data += f'\n{key}: {value}'

        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Save QR code image to a BytesIO buffer
        buffer = BytesIO()
        img.save(buffer)
        filename = f'qr_code_{self.ticket_number}.png'

        # Create a Django File object from the BytesIO buffer
        file = File(buffer, name=filename)
        self.qr_code.save(filename, file, save=False)

        super().save(*args, **kwargs)

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


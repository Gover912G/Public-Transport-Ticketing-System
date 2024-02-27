from django.contrib import admin
from .models import Ticket,Stage,Route

# Register your models here.
admin.site.register(Ticket)
admin.site.register(Stage)
admin.site.register(Route)
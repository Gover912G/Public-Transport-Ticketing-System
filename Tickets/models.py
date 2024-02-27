import uuid
from django.db import models
from Users.models import User

# Create your models here.

class Stage(models.Model):
    stage_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.stage_name

class Route(models.Model):
    route_number = models.IntegerField(blank = False)
    route_name = models.CharField(blank = False, max_length =100)
    stage = models.ManyToManyField(Stage)

    def __str__(self):
        return self.route_name

class Ticket(models.Model):
    status_choices = (
        ('Active','Active'),
        ('Completed','Completed'),
        ('Pending','Pending')
    )
    ticket_number = models.UUIDField(default = uuid.uuid4)
    route = models.ForeignKey(Route, related_name = 'route', on_delete = models.CASCADE)
    created_by = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'created_by')
    date_created = models.DateTimeField(auto_now_add = True)
    is_resolved = models.BooleanField(default = False)
    accepted_by = models.ForeignKey(User, on_delete = models.DO_NOTHING, null = True, blank = True)
    accepted_date = models.DateTimeField(null=True, blank = True)
    closed_date = models.DateTimeField(null=True, blank = True)
    ticket_status = models.CharField(max_length = 20, choices = status_choices)
    start_point = models.ForeignKey(Stage, related_name='start_point', on_delete=models.CASCADE)
    stop_point = models.ForeignKey(Stage, related_name='stop_point', on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.ticket_number
    




from django.urls import path
from . import views


app_name = 'tickets'
urlpatterns = [
    path('mytickets/<int:pk>/', views.ticket_details, name='mytickets'),
    path('book_ticket/', views.book_ticket, name='book_ticket'),
    # path('book_ticket/', views.book_ticket, name='book_ticket'),
    path('mytickets/', views.my_tickets, name='mytickets'),
    path('update_ticket/<int:pk>/', views.update_ticket, name='update_ticket'),
    path('All_tickets/', views.All_tickets, name='All_tickets'),
    path('Booked_tickets/', views.All_tickets, name='Booked_tickets'),
    path('Accept_ticket/<int:pk>/', views.All_tickets, name='Accept_ticket'),
    path('Close_ticket/<int:pk>/', views.Close_ticket, name='Close_ticket'),
    path('workspace/', views.workspace, name='workspace'),
    path('All_closed_tickets', views.All_closed_tickets, name='All_closed_tickets'),
]
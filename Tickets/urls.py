from django.urls import path

from . import views
app_name = 'tickets'
urlpatterns = [
    # path('mytickets/<int:pk>/', views.ticket_details, name='mytickets'),
    path('mytickets/<int:pk>/', views.ticket_details, name='mytickets'),

    path('book_ticket/', views.book_ticket, name='book_ticket'),
]
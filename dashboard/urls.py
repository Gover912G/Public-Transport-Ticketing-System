from django.urls import path

from . import views
app_name = 'dashboard'
urlpatterns = [
    path('', views.dashboard, name='dash'),
    path('tickets', views.Tickets, name='tickets'),
]
from django.urls import path
from . import views


app_name = 'user'
urlpatterns = [
    path('passenger_registration', views.register_passenger, name='signin'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
]
from django.urls import path
from . import views


app_name = 'user'
urlpatterns = [
    path('passenger_registration', views.register_passenger, name='signin'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('profile', views.Profile, name='profile'),
    # path('password_reset', views.password_reset, name='password_reset'),
]
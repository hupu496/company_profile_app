
from django.urls import path
from . import views

from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.registerview,name='register'),
    path('login', views.loginview,name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/',views.logoutview, name="logout"),
    path('email_request/',views.email_request, name="email_request"),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('message/',views.message,name='message'),
    path('warning/',views.warning,name='warning'),
]

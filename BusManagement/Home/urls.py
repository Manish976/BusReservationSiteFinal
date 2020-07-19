from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('search',views.search),
    path('services',views.services),
    path('about',views.about),
    path('print',views.printTicket),
    path('contact',views.contact),
    path('search/<int:id>',views.seats),
    path('search/<int:id>/checkout',views.checkout,name="checkout"),
    path('search/<int:id>/checkout/mybooking',views.myBooking),
    path('booking',views.booking,name="booking"),
    path('profile',views.profile)



]

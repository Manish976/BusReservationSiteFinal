from django.urls import path
from . import views

urlpatterns = [
    path('',views.buses),
    path('view_bus',views.bus_view),
    path('view_bus/<int:id>',views.bus_detail),
    path('view_bus/<int:id>/update',views.updateStatus),


]

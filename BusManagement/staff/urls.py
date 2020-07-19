from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard),
    path('/reservation',views.reserve,name="reserve"),
    path('/tables',views.tables,name="tables")


]

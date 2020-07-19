from django.shortcuts import render
from Buses.models import reservation,Bus_description,Seats
from django.contrib.auth.models import User


def dashboard(request):
    b=Bus_description.objects.all()
    u = User.objects.count()
    sale= reservation.objects.count()
    c=0
    for i in b:
        c=c+i.fare
    print(c)
    return render(request,"owner/index.html",{'total':c,'count':u,'sales':sale})


def reserve(request):
    r=reservation.objects.all()
    user1=[]
    seat=[]
    for i in r :
        s=Seats.objects.filter(id=i.seat_id)
        u=User.objects.filter(id=i.user_id).distinct()
        for a in s:
            seat.append(a.seat_number)

        for b in u:
            user1.append(b.username)

    print(user1)
    print(seat)
    return render(request,"customerreserve.html",{'user':user,'seat':seat})


def tables(request):
    u=User.objects.all()
    return render(request,"owner/tables.html",{'u':u})
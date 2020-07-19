from datetime import datetime, date
from operator import itemgetter

from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from Buses.models import Bus_description,reservation,Seats
from Home.models import Booking




def index(request):
    return render(request,"Home.html")



def search(request):
    if request.method=='POST':
        from1=request.POST['from']
        to1=request.POST['to']
        date1=request.POST['date']
        shift=request.POST['shift']
        bustype=request.POST['bus_type']
        cur_time=datetime.now()
        c=cur_time.strftime("%H:%M:%S")
        print("this is date",date1)
        b=Bus_description.objects.filter(From=from1,To=to1,dates=date1,Shift=shift,status=True,BusType=bustype)
        return render(request, "search.html",{'b':b,'date':date1})

    else:
        return render(request,"search.html")


def services(request):
    if request.method=='POST':
        date1=request.POST['date']
        b=Bus_description.objects.filter(dates=date1,status=1)
        return render(request,"services.html",{'data':b,'d':date1})

    else:
        date1=date.today()
        print("this is date",date1)
        b = Bus_description.objects.filter(dates=date1, status=1)
        return render(request,"services.html",{'data':b ,'d':date1})


def about(request):
    return render(request,"Aboutus.html")


def printTicket(request):
    return render(request,"print.html")


def contact(request):
    return render(request,"contact.html")


@login_required(login_url='login')
def seats(request,id):
    r=reservation.objects.filter(bus_description_id=id)
    t=r.values('seat_id')
    res = list(map(itemgetter('seat_id'), t))
    m=[]
    print(len(res))
    bus_price=Bus_description.objects.filter(id=id)
    print(bus_price)
    for i in range(0,len(res)):
        s=Seats.objects.values_list('seat_number').get(id=res[i])
        m.insert(i,s[0])

    return render(request, "seats.html", {'t': m,'i':id,'bus':bus_price})


@login_required(login_url='login')
def checkout(request,id):
     if request.user.is_authenticated:
        a=request.POST['arrayValue']
        x=a.split(',')
        b=Bus_description.objects.get(id=id)
        dates=b.dates

        for i in range(0,len(x)):
            r=reservation(bus_description_id=id,seat_id=x[i],date=dates,user_id=request.user.id)
            r.save()
        u=User.username

        r = reservation.objects.filter(user_id=request.user.id)
        seat = []
        date1 = ""
        for i in r:
            seat.append(i.seat_id)
            date1 = i.date

        seatname = []
        for h in seat:
            seatn = Seats.objects.get(id=h)
            seatname.append(seatn.seat_number)

        user1=User.objects.filter(username=u)
        return render(request,"checkout.html",{'u':user1,'seat':seatname,'date':date1})

     else:
        messages.info(request, 'success')
        return redirect('login')


@login_required(login_url='login')
def myBooking(request,id):
    name=request.POST['name']
    phone=request.POST['phone']
    address=request.POST['adrs']
    payment=request.POST['payment']
    b=Booking(Name=name,phone=phone,address=address,payment=payment)
    b.save()



    messages.info(request, 'success')

    return redirect('booking')


@login_required(login_url='login')
def booking(request):
    r=reservation.objects.filter(user_id=request.user.id)

    seat=[]
    date1=""
    bus=""
    for i in r :
        seat.append(i.seat_id)
        date1=i.date

    seatname=[]
    for h in seat:
        seatn=Seats.objects.get(id=h)
        seatname.append(seatn.seat_number)

    print(seatname)

    return render(request,"booking.html",{'seat':seatname,'date':date1})


def profile(request):
    pass






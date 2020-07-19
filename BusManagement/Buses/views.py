from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response

# Create your views here.
from Buses.models import Bus_description,reservation


def buses(request):
    if request.method=='POST':
        busname=request.POST['bus_name']
        busnum=request.POST['bus_num']
        bustype=request.POST['bus_type']
        from12=request.POST['from1']
        to12=request.POST['to1']
        shift1=request.POST['shift']
        images=request.FILES.getlist('image')
        date=request.POST['date']
        pick_time=request.POST['time']
        pick_dest=request.POST['dest']
        fare=int(request.POST['fare'])
        b1=Bus_description()
        b=Bus_description(BusName=busname,images=images,BusNumber=busnum,BusType=bustype,From=from12,To=to12,Shift=shift1,pick_time=pick_time,pick_destination=pick_dest,fare=fare)
        b.save()
        messages.info(request, 'success')
        return render(request, 'buses.html',{'form':b1})

    else:
        return render(request,'buses.html')


def bus_view(request):
    b=Bus_description.objects.all()
    return render(request,'view_bus.html',{'vws':b})


def bus_detail(request,id):
    b = Bus_description.objects.get(id=id)
    return render(request,'bus_detail.html',{'bus':b})


def updateStatus(request,id):
    status=request.POST.get('status')
    date=request.POST['date']
    b = Bus_description.objects.get(id=id)
    b.status=status
    b.dates=date
    b.save()
    return redirect('/buses/view_bus')





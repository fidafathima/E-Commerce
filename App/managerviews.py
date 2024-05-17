from django.shortcuts import render, redirect

from App.forms import RentForm, StatusForm
from App.models import Product, Rent, RentalRequest, RentalOrder


def managerPage(request):
    return render(request,'Manager_base/manager_page.html')

def rent(request):
    form=RentForm()
    if request.method=='POST':
        form1=RentForm(request.POST,request.FILES)
        if form1.is_valid():
            form1.save()
            return redirect("rent")
    return render(request,'Manager_base/rent.html',{'form':form})

def rentView(request):
    data =Rent.objects.all()
    return render(request, 'Manager_base/rent_view.html', {'data':data,})

def deleteRent(request, id):
    if request.method == 'POST':
      data =Rent.objects.get(id=id)
      data.delete()
      return redirect("rentView")


def updateRent(request,id):
    data=Rent.objects.get(id=id)
    form=RentForm(instance=data)
    if request.method=='POST':
        form1=RentForm(request.POST,instance=data)
        if form1.is_valid():
            form1.save()
            return redirect("rentView")
    return render(request,'Manager_base/update_rent.html',{'form':form})


def orders(request):
    data=RentalOrder.objects.all()
    return render(request, 'Manager_base/requests.html', {'data': data})

def orderUpdate(request,id):
    data = RentalOrder.objects.get(id=id)
    form = StatusForm(instance=data)
    if request.method == 'POST':
        status = StatusForm(request.POST, instance=data)
        if status.is_valid():
            status.save()
        return redirect('orders')
    return render(request, 'Manager_base/order_update.html', {'data': data,'form':form})
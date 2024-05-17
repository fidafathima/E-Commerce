
from django.shortcuts import render, redirect

from App.forms import CategoryForm, NotificationForm, ProductForm
from App.models import Category, Customer, Manager, Product


def adminPage(request):
    cat = Category.objects.all()
    return render(request,'Admin_base/admin_page.html',{'cat':cat})

def CategoryAdd(request):
    form=CategoryForm()
    form1 = CategoryForm(request.POST)
    if form1.is_valid():
        form1.save()
        return redirect('CategoryAdd')
    return render(request, 'Admin_base/category_add.html', {'form': form})


def ProductAdd(request):
    form = ProductForm()
    if request.method == 'POST':
        form1 = ProductForm(request.POST,request.FILES)
        if form1.is_valid():
            form1.save()
            return redirect('ProductAdd')
    return render(request, 'Admin_base/property_add.html', {'form': form})

def ProductView(request ,id):
    cat=Category.objects.get(id=id)
    data =Product.objects.filter(category=cat)
    return render(request, 'Admin_base/product_view.html', {'data':data,})


def deleteProduct(request, id):
    if request.method == 'POST':
      data =Product.objects.get(id=id)
      data.delete()
      return redirect("propertyView")


def updateProduct(request,id):
    data=Product.objects.get(id=id)
    form=ProductForm(instance=data)
    if request.method=='POST':
        form1=ProductForm(request.POST,instance=data)
        if form1.is_valid():
            form1.save()
            return redirect("ProductView")
    return render(request,'Admin_base/update_property.html',{'form':form})

def notification(request):
    data=NotificationForm()
    Form=NotificationForm(request.POST)
    if Form.is_valid():
        Form.save()
        return redirect('notification')
    return render(request, 'Admin_base/note.html', {'data': data})

def cData(request):
    data1=Customer.objects.all()
    return render(request,'Admin_base/c_data.html',{'data1':data1})

def mData(request):
    data2=Manager.objects.all()
    return render(request,'Admin_base/m_data.html',{'data2':data2})
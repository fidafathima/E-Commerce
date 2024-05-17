from django.contrib import messages
from django.shortcuts import render, redirect

from App.forms import ProductForm, DeliveryForm, RentalPaymentForm, ReviewForm
from App.models import Customer, Notification, Category, Product, Cart, Payment, Rent, RentalRequest, RentalOrder, \
    Review


def customerPage(request):
    return render(request,'Customer_base/home.html')

def base2(request):
    return render(request,'Customer_base/home2.html')


def noteView(request):
    user1=request.user
    user2=Customer.objects.get(user=user1)
    form=Notification.objects.filter(user=user2)
    return render(request,'Customer_base/note_view.html',{'form':form})

def products(request):
    cat = Category.objects.all()
    product=Product.objects.all()
    return render(request, 'Customer_base/shop.html', {'product': product,'cat':cat})




def cProductView(request,id):
    cat = Category.objects.all()
    category=Category.objects.get(id=id)
    product =Product.objects.filter(category=category)
    return render(request, 'Customer_base/shop.html', {'product':product,'cat':cat})

def oneItem(request,id):
    item=Product.objects.get(id=id)
    review = Review.objects.filter(item=item)
    return render(request, 'Customer_base/single product.html', {'item': item,'review':review})


def addCart(request,id):
    form0 = Product.objects.get(id=id)
    data=request.user
    u = Customer.objects.get(user=data)
    data1=Cart.objects.filter(user=u,item=form0)
    if data1.exists():
        messages.info(request,'you have already added')
        return redirect('cart')
    obj=Cart()
    obj.user=u
    obj.item=form0
    obj.save()
    return redirect("cart")


def cart(request):
    user1 = request.user
    user2 = Customer.objects.get(user=user1)
    data = Cart.objects.filter(user=user2)
    total=0
    c=50
    cart=[i for i in data]
    print(cart)
    if cart:
        for i in cart:
            temp=(int(i.quantity0)*i.item.cost)
            total +=int(temp)
    amount=total+c
    # print(data.save())
    return render(request, 'Customer_base/cart.html', {'data': data,'total':total,'amount':amount})

def quantity(request,id):
    data=Cart.objects.get(id=id)
    data.quantity0=int(data.quantity0)+1
    data.save()
    return redirect('cart')

def remove(request,id):
    data=Cart.objects.get(id=id)
    if int(data.quantity0)<=1:
        return redirect("cart")
    else:
        data.quantity0=int(data.quantity0)-1
        data.save()
        return redirect('cart')

def delete(request, id):
    # if request.method == 'POST':
      data =Cart.objects.get(id=id)
      data.delete()
      return redirect("cart")

def delivery(request,id):
    item = Cart.objects.get(id=id)
    user=request.user
    total=int(item.item.cost)*int(item.quantity0)+50
    customer=Customer.objects.get(user=user)
    form = DeliveryForm()
    if request.method == 'POST':
        form1 = DeliveryForm(request.POST)
        if form1.is_valid():
            obj = form1.save(commit=False)
            obj.user= customer
            obj.product=item
            obj.amount=total
            item.status=1
            item.item.quantity=int(item.item.quantity)-int(item.quantity0)
            item.save()
            obj.save()
            return redirect("thankyou")
    return render(request, 'Customer_base/checkout.html', {'form': form,'item':item,'total':total})



def rentCate(request):
    category=Category.objects.all()
    product=Rent.objects.all()
    return render(request, 'Customer_base/category.html', {'category':category,'product':product})

def rentProduct(request,id):
    category = Category.objects.all()
    data = Category.objects.get(id=id)
    product = Rent.objects.filter(category=data)
    return render(request, 'Customer_base/category.html', {'category':category,'product': product})

def oneProduct(request,id):
    item=Rent.objects.get(id=id)
    return render(request, 'Customer_base/oneRent.html', {'item': item})





def rentalRequest(request,id):
    product=Rent.objects.get(id=id)
    user=Customer.objects.get(user=request.user)
    rent=RentalRequest.objects.filter(user=user,rent=product)
    if rent.exists():
        messages.info(request,'you have already requested')
        return redirect("Renteditem")
    obj=RentalRequest()
    obj.user=user
    obj.rent=product
    obj.save()
    return redirect("Renteditem")
    # return render(request, 'Customer_base/rented.html',{'product':product} )

def Renteditem(request):
    user=request.user
    customer=Customer.objects.get(user=user)
    item = RentalRequest.objects.filter(user=customer)
    return render(request, 'Customer_base/rented.html',{'item':item} )

def quantity1(request,id):
    data=RentalRequest.objects.get(id=id)
    if int(data.quantity)>=int(data.rent.stock):
        return redirect("Renteditem")
    else:
        data.quantity=int(data.quantity)+1
        data.save()
        return redirect('Renteditem')

def remove1(request,id):
    data=RentalRequest.objects.get(id=id)
    if int(data.quantity)<=1:
        return redirect("Renteditem")
    else:
        data.quantity=int(data.quantity)-1
        data.save()
        return redirect('Renteditem')

def addDay(request,id):
    data=RentalRequest.objects.get(id=id)
    data.days=int(data.days)+1
    data.save()
    return redirect('Renteditem')

def removeDay(request,id):
    data=RentalRequest.objects.get(id=id)
    if int(data.days)<=1:
        return redirect("Renteditem")
    else:
        data.days=int(data.days)-1
        data.save()
        return redirect('Renteditem')



def checkout(request,id):
    items = RentalRequest.objects.get(id=id)
    total = items.rent.price * items.quantity * items.days
    amount = total + 50
    user=request.user
    customer=Customer.objects.get(user=user)
    address=RentalRequest.objects.filter(user=customer)
    form = RentalPaymentForm()
    if request.method == 'POST':
        form1 = RentalPaymentForm(request.POST)
        if form1.is_valid():
            obj = form1.save(commit=False)
            obj.user= customer
            obj.items=items
            obj.amount=amount
            obj.save()
            stock=items.rent.stock - int(items.quantity)
            items.rent.stock=stock
            items.save()
            print(stock)
            return redirect("thankyou")
    return render(request, 'Customer_base/delivery.html', {'form': form,'address':address,'amount':amount})

def thankyou(request):
    return render(request, 'Customer_base/thankyou.html',)

def orderDetails(request):
    user=Customer.objects.get(user=request.user)
    order=RentalOrder.objects.filter(user=user)
    return render(request, 'Customer_base/Order_details.html',{'order':order} )

def orderDetails2(request):
    user=Customer.objects.get(user=request.user)
    order=Payment.objects.filter(user=user)
    return render(request, 'Customer_base/orders.html',{'order':order} )

def cancelRent(request,id):
    # if request.method=='POST':
        item=RentalOrder.objects.get(id=id)
        print(item)
        item.cancel=1
        item.save()
        return redirect("orderDetails")

def review(request,id):
    item=Product.objects.get(id=id)
    user=request.user
    customer=Customer.objects.get(user=user)
    form = ReviewForm()
    if request.method=='POST':
        Form1= ReviewForm(request.POST,request.FILES)
        if Form1.is_valid():
            obj=Form1.save(commit=False)
            obj.user=customer
            obj.item=item
            obj.save()
            return redirect('thankyou')
    return render(request, 'Customer_base/review.html', {'form': form})

def customerProfile(request):
    user=request.user
    form1=Customer.objects.get(user=user)
    return render(request, 'Customer_base/profile.html', {'form1': form1})
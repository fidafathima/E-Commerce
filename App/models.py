from django.contrib.auth.models import AbstractUser
from django.db import models
# from location_field.models.plain import PlainLocationField


# Create your models here.
class Login(AbstractUser):
  is_worksmanager = models.BooleanField(default=False)
  is_customer = models.BooleanField(default=False)


class Customer(models.Model):
  user = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='customer')
  name = models.CharField(max_length=100)
  contact_no = models.CharField(max_length=100)
  email = models.EmailField()
  address = models.TextField(max_length=200)

  def __str__(self):
    return self.name

class Manager(models.Model):
  user=models.ForeignKey(Login,on_delete=models.CASCADE,related_name='workmanager')
  name = models.CharField(max_length=100)
  email = models.EmailField()
  address = models.TextField(max_length=200)
  mobile= models.CharField(max_length=100,null=False)
  document = models.FileField(upload_to='documents/')

  def __str__(self):
    return self.name

class Category(models.Model):
  category1=models.CharField(max_length=50)

  def __str__(self):
    return self.category1


class Product(models.Model):
  category=models.ForeignKey(Category,on_delete=models.CASCADE)
  name=models.CharField(max_length=100)
  brand=models.CharField(max_length=100)
  description=models.TextField(max_length=100)
  image=models.FileField(upload_to='documents/')
  image2 = models.FileField(upload_to='documents/',null=True)
  image3 = models.FileField(upload_to='documents/',null=True)
  quantity=models.PositiveIntegerField(default=0)
  cost=models.PositiveIntegerField(null=True)

  def __str__(self):
    return self.name

  def __str1__(self):
    return self.cost


class Notification(models.Model):
  user=models.ForeignKey(Customer,on_delete=models.DO_NOTHING,null=True)
  title=models.CharField(max_length=50)
  date=models.DateField(auto_now=True)



class Cart(models.Model):
  user = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
  item = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
  quantity0=models.CharField(max_length=15,default=1)
  status = models.CharField(default=0)

class Payment(models.Model):
  user = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
  product=models.ForeignKey(Cart,on_delete=models.DO_NOTHING)
  date = models.DateField(auto_now=True)
  amount= models.CharField(max_length=15)
  place=models.CharField(max_length=50)
  landmark= models.CharField(max_length=50)
  pincode = models.CharField(max_length=50)
  mobile = models.CharField(max_length=50)
  cash_delivery=models.BooleanField(default=False)
  choice = (('Order Confirmed', 'Order Confirmed'), ('Shipped', 'Shipped'))
  status = models.CharField(choices=choice,default="Order Confirmed")
  cancel_order= models.CharField(default=0)


class Review(models.Model):
  user = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
  item = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
  date=models.DateField(auto_now=True)
  subject=models.TextField()
  image=models.FileField(upload_to="documents/",null=True)

class Complaints(models.Model):
  user = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
  date=models.DateField(auto_now=True)
  subject=models.TextField()

class Rent(models.Model):
  category=models.ForeignKey(Category,on_delete=models.DO_NOTHING)
  product=models.CharField(max_length=100)
  description=models.TextField()
  brand=models.CharField(max_length=100)
  code=models.CharField(max_length=20)
  price=models.IntegerField()
  image=models.FileField(upload_to="documents/",blank=True)
  stock=models.IntegerField()


class RentalRequest(models.Model):
  user=models.ForeignKey(Customer,on_delete=models.DO_NOTHING)
  rent=models.ForeignKey(Rent,on_delete=models.DO_NOTHING)
  status=models.CharField(max_length=10,default=0)
  days=models.IntegerField(default=1)
  quantity=models.IntegerField(default=1)


class RentalOrder(models.Model):
  user = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
  items = models.ForeignKey(RentalRequest, on_delete=models.DO_NOTHING)
  date = models.DateField(auto_now=True)
  return_date=models.DateField()
  amount = models.CharField(max_length=15)
  place = models.CharField(max_length=50)
  landmark = models.CharField(max_length=50)
  pincode = models.CharField(max_length=50)
  mobile = models.CharField(max_length=50)
  cash_delivery = models.BooleanField(default=False)
  choice=(('Order Confirmed','Order Confirmed'),('Shipped','Shipped'))
  status = models.CharField(choices=choice,default="Order Confirmed")
  cancel=models.CharField(max_length=10,default=0)



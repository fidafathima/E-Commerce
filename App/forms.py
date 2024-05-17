from django import forms
from django.contrib.auth.forms import UserCreationForm


from App.models import Login, Manager, Customer, Category, Notification, Product, Payment, Rent, RentalRequest, \
    RentalOrder, Review


class LoginForm(UserCreationForm):
    username=forms.CharField()
    password1=forms.CharField(label='password',widget=forms.PasswordInput)
    password2=forms.CharField(label='confirm password',widget=forms.PasswordInput)

    class Meta:
        model=Login
        fields=('username','password1','password2')


class customerForm(forms.ModelForm):
    class Meta:
        model =Customer
        fields = ('name','contact_no','email','address')

class ManagerForm(forms.ModelForm):
    class Meta:
        model =Manager
        fields = ('name','email','address','mobile','document')

class CategoryForm(forms.ModelForm):
    class Meta:
        model=(Category)
        fields=('category1',)

class ProductForm(forms.ModelForm):
    class Meta:
        model=(Product)
        fields=("__all__")


class NotificationForm(forms.ModelForm):
    class Meta:
        model=(Notification)
        fields=("__all__")

class DeliveryForm(forms.ModelForm):
    class Meta:
        model=(Payment)
        fields=('place','landmark','pincode','mobile','cash_delivery')



class RentForm(forms.ModelForm):
    class Meta:
        model=(Rent)
        fields=("__all__")

class RentalPaymentForm(forms.ModelForm):
    class Meta:
        model=(RentalOrder)
        fields = ('place','landmark','pincode','mobile','cash_delivery',)

class StatusForm(forms.ModelForm):
    class Meta:
        model=(RentalOrder)
        fields = ('status',)

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields =('subject','image')

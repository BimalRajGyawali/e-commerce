from django import forms
from .models import User, Address, CardDetails


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = '__all__'



class UserLoginForm(forms.Form):
    name = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        exclude = ['user']

class CreditCardForm(forms.ModelForm):
    class Meta:
        model = CardDetails
        exclude = ['user']
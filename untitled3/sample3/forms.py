from django.forms import ModelForm, inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Customer, Address


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        exclude = ()


class AddressForm(ModelForm):
    class Meta:
        model = Address
        exclude = ()

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)




AddressFormSet = inlineformset_factory(Customer, Address,
                                            form=AddressForm, extra=1)
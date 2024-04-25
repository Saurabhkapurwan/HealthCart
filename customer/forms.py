from django import forms
from customer.models import *

class MyUserForm(forms.ModelForm):

    class Meta:
        model = MyUser
        fields = ('firstname', 'lastname','email','age','country','mobilenumber')
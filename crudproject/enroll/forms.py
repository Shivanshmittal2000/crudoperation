from django.core import validators
from django import forms
from django.db.models.base import Model
from django.forms.models import ModelForm
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields=['id','name','email','password']
        widgets={
        'name' : forms.TextInput(attrs={'class':'form-control'}),
        'email' : forms.EmailInput(attrs={'class':'form-control'}),
        'password' : forms.PasswordInput(attrs={'class':'form-control'}),
        }
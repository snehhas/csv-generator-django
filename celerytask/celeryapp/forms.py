from turtle import textinput
from django.forms import *
from .models import *

class CustomForm(ModelForm):
    class Meta:
        model = Details
        fields = '__all__'
        widgets={
            'name':TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'count':NumberInput(
                attrs={
                    'class':'form-control'
                }
            )
        }
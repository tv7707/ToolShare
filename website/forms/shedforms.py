from django import forms
from django.forms import TextInput, PasswordInput

from website.models.users import User
from website.models.tools import *
from .. import models

class CreateShed(forms.ModelForm):
    class Meta:
        model = models.tools.CommunityShed

        fields = ['ShedName','ShedStreetAddress']
        widgets = {
            'ShedName': TextInput(attrs={'required': True, 'class': 'form-control'}),
            'ShedStreetAddress': TextInput(attrs={'required': True, 'class': 'form-control'}),
            #'ShedStreetAddress2': TextInput(attrs={'required': False}),
            #'ShedCity': TextInput(attrs={'required': True}),
            #'ShedState': TextInput(attrs={'required': True}),
            #'ShedZip': TextInput(attrs={'required': True}),
        }

    def __init__(self, *args, **kwargs):
        super(CreateShed, self).__init__(*args, **kwargs)
from django import forms
from django.db import models
from django import forms
from django.forms import ModelForm, Textarea, TextInput, PasswordInput, Select, DateTimeField

from website.models.users import User
from .. import models

class PersonalManagementForm(forms.ModelForm):
    class Meta:
        model = models.users.User

        fields = ['Email','First_Name','Last_Name','Date_of_Birth','Address_Line1','Address_Line2','City','State','ZIP_Code','Country','Phone_Number','Pickup_Arrangment', 'Preferred_Contact' ]
        widgets = {
            'Email': TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
            'First_Name': TextInput(attrs={'required': True, 'class': 'form-control'}),
            'Last_Name': TextInput(attrs={'required': True, 'class': 'form-control'}),
            # 'Password': PasswordInput(attrs={'required': True}),
            'Date_of_Birth': TextInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
            'Address_Line1': TextInput(attrs={'required': True, 'class': 'form-control'}),
            'Address_Line2': TextInput(attrs={'required': False, 'class': 'form-control'}),
            'City': TextInput(attrs={'required': True, 'class': 'form-control'}),
            'State': Select(attrs={'required': True, 'class': 'form-control'}),
            'ZIP_Code': TextInput(attrs={'required': True, 'class': 'form-control'}),
            'Country': TextInput(attrs={'required': True, 'class': 'form-control'}),
            'Phone_Number': TextInput(attrs={'required': True, 'class': 'form-control'}),
            'Pickup_Arrangment': TextInput(attrs={'required': True, 'class': 'form-control'}),
            'Preferred_Contact': TextInput(attrs={'required': True, 'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(PersonalManagementForm, self).__init__(*args, **kwargs)


class ChangePassword(forms.ModelForm):
    Password = forms.CharField(label='New password',max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(label='Confirm password', max_length=20, widget=forms.PasswordInput(attrs={
        'class': 'form-control'}))

    class Meta:
        model = models.users.User

        fields = []
        widgets = {

        }

    def __init__(self, *args, **kwargs):
        super(ChangePassword, self).__init__(*args, **kwargs)


    def clean_confirm_password(self):
        if not self.cleaned_data["Password"] == self.cleaned_data["confirm_password"]:
            raise forms.ValidationError("Passwords do not match.")
        return self.cleaned_data["confirm_password"]

class Registration(forms.ModelForm):

    confirm_password = forms.CharField(label='Confirm password', max_length=20, widget=forms.PasswordInput(attrs={
        'class': 'form-control'}))
    Address_Line2 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = models.users.User

        fields = ['First_Name','Last_Name','Date_of_Birth', 'Email','Password','confirm_password','Address_Line1','Address_Line2','City','State','ZIP_Code','Country','Phone_Number','Pickup_Arrangment', 'Preferred_Contact' ]
        widgets = {
            'First_Name': TextInput(attrs={'required': True, 'class': 'form-control', "placeholder": 'eg: John'}),
            'Last_Name': TextInput(attrs={'required': True, 'class': 'form-control', "placeholder": 'eg: Doe'}),
            #'Age': forms.DateInput(attrs={'class':'form-control', 'id': 'datetimepicker'}),
            'Date_of_Birth': TextInput(attrs={'required': True, 'class': 'form-control',"placeholder": 'mm/dd/yyyy'}),
            'Password': PasswordInput(attrs={'required': True, 'class': 'form-control', "placeholder": ''}),
            'Email': forms.TextInput(attrs={'class': 'form-control', "placeholder": 'your@mail.com'}),
            'Address_Line1': TextInput(attrs={'required': True, 'class': 'form-control', "placeholder": 'eg: 123 Main St'}),
            'City': TextInput(attrs={'required': True, 'class': 'form-control', "placeholder": 'eg: Rochester'}),
            'State': Select(attrs={'required': True, 'class': 'form-control'}),
            'ZIP_Code': TextInput(attrs={'required': True, 'class': 'form-control',"placeholder": 'eg: 12345'}),
            'Country': TextInput(attrs={'required': True, 'class': 'form-control', "placeholder": 'eg: United States'}),
            'Phone_Number': TextInput(attrs={'required': True, 'class': 'form-control',"placeholder": '+0123456789'}),
            'Pickup_Arrangment': Select(attrs={'required': True, 'class': 'form-control'}),
            'Preferred_Contact': Select(attrs={'required': True, 'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(Registration, self).__init__(*args, **kwargs)


    def clean_confirm_password(self):
        if not self.cleaned_data["Password"] == self.cleaned_data["confirm_password"]:
            raise forms.ValidationError("Passwords do not match.")
        return self.cleaned_data["confirm_password"]


class Login(forms.Form):
    Email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', "placeholder": 'your@mail.com'}))
    Password = forms.CharField(widget=forms.TextInput(attrs={'type': 'password', 'class': 'form-control'}))


class RecoverPassword(forms.Form):
    Email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))

class ToolRegistration(forms.ModelForm):
    class Meta:
        model = models.tools.Tool

        fields = ['Tool_Name','Description','Condition','Share_location','picture' ]
        widgets = {
            'Tool_Name': TextInput(attrs={'required': True}),
            'Description': TextInput(attrs={'required': True}),
           'Condition': TextInput(attrs={'required': True}),
            #'Share_location_type': TextInput(attrs={'required': False}),
            'Share_location': Select(attrs={'required': True}),
            'picture': forms.FileInput(attrs={'class': 'form-control'}),

        }

    def __init__(self, *args, **kwargs):
        super(ToolRegistration, self).__init__(*args, **kwargs)


class Borrowform(forms.Form):
    Email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    Password = forms.CharField(widget=forms.TextInput(attrs={'type': 'password', 'class': 'form-control'}))


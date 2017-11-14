#from django import forms
from django.forms import TextInput, PasswordInput
from . import models

#class Registration(forms.ModelForm):

 #   confirm_password = forms.CharField(label='Confirm password', max_length=30, widget=forms.PasswordInput(attrs={
 #       'class': 'form-control'}))
 #   class Meta:
 #       model = models.users.User

  #      fields = ['First_Name','Last_Name','Password','confirm_password','Email','Address_Line1','Address_Line2','City','State','ZIP_Code','Country','Phone_Number','Pickup_Arrangment', 'Preferred_Contact' ]
   #     widgets = {
     #       'First_Name': TextInput(attrs={'required': True}),
    #        'Last_Name': TextInput(attrs={'required': True}),
      #      'Password': PasswordInput(attrs={'required': True}),
       #     #'Email': forms.TextInput(attrs={'required': True, 'placeholder': "your@mail.com"}),
        #    'Email': forms.TextInput(attrs={'class': 'form-control', "placeholder": 'Enter title here'}),
         #   'Address_Line1': TextInput(attrs={'required': True}),
          #  'Address_Line2': TextInput(attrs={'required': False}),
           # 'City': TextInput(attrs={'required': True}),
            #'State': TextInput(attrs={'required': True}),
            #'ZIP_Code': TextInput(attrs={'required': True}),
            #'Country': TextInput(attrs={'required': True}),
            #'Phone_Number': TextInput(attrs={'required': True}),
            #'Pickup_Arrangment': TextInput(attrs={'required': True}),
            #'Preferred_Contact': TextInput(attrs={'required': True})
        #}

#    def __init__(self, *args, **kwargs):
#       super(Registration, self).__init__(*args, **kwargs)


#    def clean_confirm_password(self):
#        if not self.cleaned_data["password"] == self.cleaned_data["confirm_password"]:
#            raise forms.ValidationError("Passwords do not match.")
#        return self.cleaned_data["confirm_password"]


#class Login(forms.Form):
#    Email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#    Password = forms.CharField(widget=forms.TextInput(attrs={'type': 'password', 'class': 'form-control'}))

# class Tools(forms.ModelForm):
#     class Meta:
#         model = models.tools.Tool
#
#         fields = ['owner','description','special_instructions','color','identifier','is_active','pickup_arrangements','share_location_type','share_location']
#         widgets = {
#             'owner': TextInput(attrs={'required': True}),
#             'description': TextInput(attrs={'required': True}),
#             'special_instructions': PasswordInput(attrs={'required': True}),
#             'color': TextInput(attrs={'required': True}),
#             'identifier': TextInput(attrs={'required': True}),
#             'is_active': TextInput(attrs={'required': False}),
#             'pickup_arrangements': TextInput(attrs={'required': True}),
#             'share_location_type': TextInput(attrs={'required': True}),
#             'share_location': TextInput(attrs={'required': True})
#         }
#
#     def __init__(self, *args, **kwargs):
#         super(Registration, self).__init__(*args, **kwargs)


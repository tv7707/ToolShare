from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.contrib.auth.models import User as DjangoUser

from website import forms, models
from website.forms.usersforms import Registration

from website.models.users import User
def register(request):
    registration_form = Registration(request.POST or None)

    if registration_form.is_valid():

        myuser = User()
        myuser.First_Name = registration_form.cleaned_data['First_Name']
        myuser.Last_Name = registration_form.cleaned_data['Last_Name']
        myuser.Password = registration_form.cleaned_data['Password']
        myuser.Email = registration_form.cleaned_data['Email']
        myuser.Date_of_Birth = registration_form.cleaned_data['Date_of_Birth']
        myuser.Address_Line1 = registration_form.cleaned_data['Address_Line1']
        myuser.Address_Line2 = registration_form.cleaned_data['Address_Line2']
        myuser.City = registration_form.cleaned_data['City']
        myuser.State = registration_form.cleaned_data['State']
        myuser.ZIP_Code = registration_form.cleaned_data['ZIP_Code']
        myuser.Country = registration_form.cleaned_data['Country']
        myuser.Phone_Number = registration_form.cleaned_data['Phone_Number']
        myuser.Pickup_Arrangment = registration_form.cleaned_data['Pickup_Arrangment']
        myuser.Preferred_Contact = registration_form.cleaned_data['Preferred_Contact']
        myuser.save()

        django_user = DjangoUser.objects.create_user(registration_form.cleaned_data['Email'],
                                                     registration_form.cleaned_data['Email'],
                                                     registration_form.cleaned_data['Password'])
        django_user.save()
        return HttpResponseRedirect('/login')

    reg_context = {
        'reg_form': registration_form,
    }

    return render(request, 'register.html', reg_context)
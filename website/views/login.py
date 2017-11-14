from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout

from website import forms, models
from website.forms.usersforms import Login
from website.models.users import User
from website.models.tools import CommunityShed

def index(request):
    login_form = Login(request.POST or None)
    page_context = {
        'login_form': login_form,
    }
    return render(request, 'index.html', page_context)
#
# def login(request):
#     login_form = Login(request.POST or None)
#
#     login_context = {
#         'login_form': login_form,
#     }
#     print(login_form.is_valid())
#
#     if login_form.is_valid():
#         email = login_form.cleaned_data['Email']
#         password = login_form.cleaned_data['Password']
#         user = User.objects.filter(Email=email, Password=password)
#         if user is not None:
#             # django_login(request, user)
#             return HttpResponseRedirect('http://127.0.0.1:8000/dashboard/')
#         else:
#             login_context['error'] = 'Invalid Credentials.'
#
#     return render(request, 'login.html', login_context)

def login(request):
    login_form = Login(request.POST or None)
    login_context = {
        'login_form': login_form,
    }

    if login_form.is_valid():
        login_obj = User.objects.filter(Email=login_form.cleaned_data['Email'],
                                        Password=login_form.cleaned_data['Password'])
        if login_obj:
            user = User.objects.get(Email=login_form.cleaned_data['Email'],
                                        Password=login_form.cleaned_data['Password'])
            shed = CommunityShed.objects.filter(ShedZip = user.ZIP_Code)
        if not login_obj:
            login_context['error'] = 'Invalid Credentials!'
        elif shed:
            request.session['open'] = True
            request.session['Email'] = login_form.cleaned_data['Email']
            request.session['First_Name']  = user.First_Name;
            return HttpResponseRedirect('/dashboard/')
        else:
            request.session['open'] = True
            request.session['Email'] = login_form.cleaned_data['Email']
            return HttpResponseRedirect('/communitycreate/')
    return render(request, 'login.html', login_context)

# def logout(request):
#     django_logout(request)
#     return HttpResponseRedirect('http://127.0.0.1:8000/')


def logout(request):
    request.session['open'] = False
    return HttpResponseRedirect('/login/')


def is_logged_in(request):
    if request.session['open'] != True:
        return None
    else:
        # request.session.flush()
        django_user = request.session['Email']
        # request.session.flush()
        user = User.objects.get(Email=django_user)
        return user




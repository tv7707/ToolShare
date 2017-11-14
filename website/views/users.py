from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.views import login
from django.contrib.auth import views
from website import forms
from website.views.community import numnotify
from website.forms.usersforms import PersonalManagementForm, ChangePassword, RecoverPassword
from website.models.users import User
import random

#class PersonalManagementView(forms.Form):
from website.views.login import is_logged_in
from django.core.mail import EmailMessage


def change_password(request):
    template_response = views.password_change(request)
    print(template_response)
    # Do something with `template_response`
    return HttpResponseRedirect('/dashboard')

def personalmanagemnet(request):
    myuser = is_logged_in(request)
    print(myuser)
    if not myuser:
        return HttpResponseRedirect("/login/")

    no_notification = max(numnotify(request) - myuser.seen, 0)
    personalmanagemnet_form = PersonalManagementForm(request.POST or None, instance=myuser)
    if personalmanagemnet_form.is_valid():
        personalmanagemnet_form.save()
        return HttpResponseRedirect('/dashboard')

    update_context = {
        'update_form': personalmanagemnet_form,
        'no_notification':no_notification
    }
    return render(request, 'personalmanagemnet.html', update_context )


def changepassword(request):
    myuser = is_logged_in(request)
    if not myuser:
        return HttpResponseRedirect("/login/")
    changepassword_form = ChangePassword(request.POST or None, instance=myuser)

    if changepassword_form.is_valid():
        print(myuser.Password)
        myuser.Password = changepassword_form.cleaned_data['Password']
        # print(changepassword_form.cleaned_data['Password'])
        print(myuser.Password)
        # myuser.save()
        changepassword_form.save()
        # login.password_change(request, template_name='templates/changepassword.html', post_change_redirect=None,
        #                 password_change_form=ChangePassword, current_app=None, extra_context=None)
        return HttpResponseRedirect('/dashboard')

    no_notification = max(numnotify(request) - myuser.seen,0)
    page_context = {
        'changepassword_form': changepassword_form,
        'no_notification':no_notification
    }
    return render(request, 'changepassword.html', page_context)

def recoverpassword(request):
    changepassword_form = RecoverPassword(request.POST or None)

    if changepassword_form.is_valid():
        email = changepassword_form.cleaned_data['Email']
        user = User.objects.filter(Email=email)
        if user is not None:
            newpass = ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(10))
            user_obj = User.objects.get(Email=email)
            user_obj.Password = newpass
            user_obj.save()

            message = "Hello " + user_obj.First_Name + ",\n\n"
            message += "Your new password is:\n"
            message += newpass + "\n"
            message += "Thanks \n"
            #print(user_obj)
            email1 = EmailMessage('[Toolshare] - New password', message, to=[email])
            email1.send()

            new_context = {
                'Email': email ,
                'Password': newpass,
            }

            #new_context = {
            #    'Email': user_obj.First_Name ,
            #    'Password': newpass,
            #}
            return render(request, 'showpassword.html', new_context)

        return HttpResponseRedirect('/recoverpassword/')

    page_context = {
        'changepassword_form': changepassword_form,
    }
    return render(request, 'recoverpassword.html', page_context)
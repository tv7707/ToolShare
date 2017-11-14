from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from website.views.login import is_logged_in
from website import forms, models
from website.views.community import numnotify
from website.models.tools import *
from datetime import *

from website.forms.shedforms import *

from website.models.tools import CommunityShed

def communitycreate(request):
    #get the active user
    print("creating shed")
    user = is_logged_in(request)

    #if no user is logged in
    if not user:

        #direct them to the login page
        return HttpResponseRedirect("/login/")
        #create a new registration form
    reg_form = CreateShed(request.POST or None)
    print("the form:\n")
    print(reg_form)
    #if the form was successfully created
    if reg_form.is_valid():
        print("valid form")
        #create the shed and fill the attributes
        shed_obj = CommunityShed()
        shed_obj.ShedName = reg_form.cleaned_data['ShedName']
        shed_obj.ShedStreetAddress = reg_form.cleaned_data['ShedStreetAddress']
        # shed_obj.ShedStreetAddress2 = reg_form.cleaned_data['ShedStreetAddress2']
        #From here downwards we retrieve info from user and fill the table
        shed_obj.ShedCity =  user.City
        shed_obj.ShedState =  user.State
        shed_obj.ShedZip =  user.ZIP_Code
        shed_obj.ShedCoord = user
        shed_obj.save()
        print("printing shed")
        print(shed_obj)
        #send the user back to the dashboard
        return HttpResponseRedirect('/dashboard/')

    if "cancel" in request.POST:
        return HttpResponseRedirect('/login/')

    reg_context = {
        'reg_form': reg_form,
        'user': user,
    }
    print(reg_form)
    print("returning the render")
    #send the user to the shed creation form
    return render(request, 'communitycreate.html', reg_context)

def sharechange(request):
    user = is_logged_in(request)
    shed = CommunityShed.objects.filter(ShedZip = user.ZIP_Code)
    print(shed)
    if not user:
        return HttpResponseRedirect("/login/")

    no_notification = max(numnotify(request) - user.seen, 0)
    all_tools = Tool.objects.filter(Owner = user)
    context = {
        'all_tools': all_tools,
        'user': user,
        'shed': shed,
        'no_notification':no_notification
    }

    if 'share' in request.POST:
    #if request.method == "POST":
        tool = Tool()
        tool_name = ""
        try:
            tool_name = request.POST['share']
            print(tool_name)
        except:
            print("no item supplied")
        tool = Tool.objects.get(Tool_Name = tool_name, Owner = user)
        print(tool.Is_active)
        if tool.Share_location == "H":
            tool.Share_location = "S"
        elif tool.Share_location == "S":
            tool.Share_location = "H"
        tool.save()

        return render(request, 'sharechange.html', context)
    if 'update' in request.POST:
        tool = Tool()
        tool_name = ""
        try:
            tool_name = request.POST['update']
            print(tool_name)
        except:
            print("no item supplied")
        tool = Tool.objects.get(Tool_Name = tool_name)
        print(tool.Is_active)
        from_date = request.POST["from_date"]
        to_date = request.POST["to_date"]
        tool.avail_from = from_date
        tool.avail_to = to_date
        print("HERE" +str(tool.avail_to))
        tool.save()
    if 'available' in request.POST:
    #if request.method == "POST":
        tool = Tool()
        tool_name = ""
        try:
            tool_name = request.POST['available']
            print(tool_name)
        except:
            print("no item supplied")
        tool = Tool.objects.get(Tool_Name = tool_name, Owner = user)
        print(tool.Is_active)
        if tool.Is_active == True:
            tool.Is_active = False
        elif tool.Is_active == False:
            tool.Is_active = True
        tool.save()

        return render(request, 'sharechange.html', context)
    else:
        return render(request, 'sharechange.html', context)

def share(request):
    user = is_logged_in(request)
    if not user:
        return HttpResponseRedirect("/login/")

    # showing list of all tools available for borrowing excluding the tools owned by user
    all_tools = Tool.objects.filter(Owner = user)
    context = {
        'all_tools': all_tools,
    }

    if request.method == "POST":
        try:
            tool_id = request.GET['id']
            print(tool_id)
        except:
            print("no id supplied")

        from_date = request.POST["from_date"]
        to_date = request.POST["to_date"]
        share_date = request.POST["share_date"]
        post_message= request.POST["message"]
        print("From date: " + from_date + " to date: " +to_date)

        #Now I am writing everything I got from the html form into the database
        tool = Tool.objects.get(id=tool_id)
        tool.avail_from=from_date
        tool.avail_to= to_date
        tool.share_date = share_date
        tool.message = post_message
        tool.save()
        print("From date: " + str(tool.avail_from) + " to date: " + str(tool.avail_to) + "Message: " + tool.message + "share date: " + str(tool.share_date))
        print(str(tool.avail_from))
        return HttpResponseRedirect('/dashboard/')
    else:
        return render(request, 'share.html', context)
def choice(request):
    user = is_logged_in(request)
    if not user:
        return HttpResponseRedirect("/login/")
    try:
        shdname=request.POST['choic']
        shed = CommunityShed.objects.get(ShedName=shdname)
        print('Chosen shed is ' + shdname)
        shed.is_Active = True
        shed.save()
    except(KeyError):
        all_sheds = CommunityShed.objects.filter(is_Active= False)
        #print(all_objects)
        context = {
            'all_sheds': all_sheds,
        }
        return render(request, 'choice.html', context)
    else:

        return render(request, 'dashboard.html')
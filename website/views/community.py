from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from website import forms
from website.forms.usersforms import ToolRegistration
from website.models.users import User
from website.views.login import is_logged_in
from website.models.tools import Tool, Sharedtool, CommunityShed
from datetime import datetime, date


# Create your views here.


def statistics(request):
    user = is_logged_in(request)
    if not user:
        return HttpResponseRedirect("/login/")

        # return HttpResponse('This is community shed page.')
    all_objects = User.objects.all()
    print(all_objects)
    no_notification = max(numnotify(request) - user.seen,0)
    context = {
        'all_objects': all_objects,
        'no_notification':no_notification
    }
    return render(request, 'statistics.html', context)


def registertool(request):
    user = is_logged_in(request)
    if not user:
        return HttpResponseRedirect("/login/")

    registration_form = ToolRegistration(request.POST or None, request.FILES or None)
    if registration_form.is_valid():
        print('success')
        default_date = request.POST["default_date"]
        user_obj = Tool()
        user_obj.Tool_Name = registration_form.cleaned_data['Tool_Name']
        user_obj.Description = registration_form.cleaned_data['Description']
        user_obj.Condition = registration_form.cleaned_data['Condition']
        user_obj.Share_location = registration_form.cleaned_data['Share_location']
        user_obj.avail_from = default_date
        user_obj.avail_to = default_date
        user_obj.share_date = default_date
        user_obj.Owner = user
        user_obj.shed = CommunityShed.objects.get(ShedZip=user.ZIP_Code)
        # user_obj.Share_location_type = registration_form.cleaned_data['Share_l
        user_obj.picture = request.FILES['picture']
        # user_obj.Share_location_type = registration_form.cleaned_data['Share_location_type']
        user_obj.save()

        return HttpResponseRedirect('/dashboard/')

    no_notification = max(numnotify(request) - user.seen, 0)
    reg_context = {
        'reg_form': registration_form,
        'no_notification': no_notification
    }

    return render(request, 'registertool.html', reg_context)


def listtool(request):
    user = is_logged_in(request)
    if not user:
        return HttpResponseRedirect("/login/")

    no_notification = max(numnotify(request) - user.seen, 0)
    all_tools = Tool.objects.filter(Is_active=True)
    brtool = Sharedtool.objects.all()

    # print(all_objects)
    context = {
        'all_tools': all_tools,
        'brtool': brtool,
        'no_notification':no_notification
    }
    return render(request, 'listtool.html', context)


def borrow(request):
    user = is_logged_in(request)
    if not user:
        return HttpResponseRedirect("/login/")

    # showing list of all tools available for borrowing excluding the tools owned by user
    user_shed = CommunityShed.objects.get(ShedZip=user.ZIP_Code)
    all_tools = Tool.objects.filter(Is_active=True, shed=user_shed).exclude(Owner=user)
    no_notification = max(numnotify(request) - user.seen, 0)
    context = {
        'all_tools': all_tools,
        'no_notification':no_notification
    }

    if request.method == "POST":
        try:
            tool_id = request.GET['id']
            print(tool_id)
        except:
            print("no id supplied")

        from_date = request.POST["from_date"]
        from_date = datetime.strptime(from_date, "%Y-%m-%d").date()
        to_date = request.POST["to_date"]
        to_date = datetime.strptime(to_date, "%Y-%m-%d").date()
        post_message = request.POST["message"]

        if from_date > to_date:
            return HttpResponse("Please select a valid date range.")

        # Now I am writing everything I got from the html form into the database

        borrow_tool = Tool.objects.get(id=tool_id)
        share_tool = Sharedtool()
        share_tool.Borrower = user
        share_tool.atool = borrow_tool
        share_tool.start_date = from_date
        share_tool.end_date = to_date
        share_tool.message = post_message

        # Check if the tool is at shed or at home and set the status accordingly
        if borrow_tool.Share_location == 'H':
            share_tool.status = 'BorrowRequest'
        else:
            share_tool.status = 'Borrowed'

        # if the tools is already borrowed by other user ask user to reselect another date.
        try:
            existing_borrower_list = Sharedtool.objects.filter(atool_id=borrow_tool).filter(status__contains='Borrow')
            for existing_borrower in existing_borrower_list:

                # Test if the selected tool is available on dates requested by the user
                if (existing_borrower.start_date <= from_date and from_date <= existing_borrower.end_date or
                                existing_borrower.start_date <= to_date and to_date <= existing_borrower.end_date or
                                from_date <= existing_borrower.start_date and existing_borrower.start_date <= to_date or
                                from_date <= existing_borrower.end_date and existing_borrower.end_date <= to_date):
                    return HttpResponse(
                        "The tool you requested is not available on this date, please select another date.")

        except ObjectDoesNotExist:
            pass  # no need to check
        else:
            pass
        share_tool.save()

        return HttpResponseRedirect('/dashboard/')
    else:
        return render(request, 'borrow.html', context)


        # bortool = Tool.objects.get(ToolName=tlname)
        # print('Borrowed tool is ' + tlname)
        # share_tool=Sharedtool()
        # share_tool.Borrower=user
        # share_tool.atool=bortool
        # share_tool.save()


def mytools(request):
    user = is_logged_in(request)
    if not user:
        return HttpResponseRedirect("/login/")
    noneuser = User.objects.get(First_Name='No')
    try:
        tlname = request.POST['choice']
        rettool = Tool.objects.get(Tool_Name=tlname)

        rettool.Is_available = True
        rettool.Borrower = noneuser
        rettool.save()
    except(KeyError):
        merotools = Tool.objects.filter(Owner=user)
        print(merotools)
        no_notification = max(numnotify(request) - user.seen, 0)
        context = {
            'merotools': merotools,
            'no_notification':no_notification
        }
        return render(request, 'mytools.html', context)
    else:

        return HttpResponseRedirect('/dashboard/')


def borroweditems(request):
    user = is_logged_in(request)
    if not user:
        return HttpResponseRedirect("/login/")

    # noneuser = User.objects.get(First_Name='No')
    try:
        toolid = request.POST['choice']

        # adding row id for filtering out duplicate results and returning only the selected item
        toolrowid = request.POST['rowid']
        returntool = Sharedtool.objects.get(atool_id=toolid, status='Borrowed', id=toolrowid)
        returntool.status = 'ReturnRequest'
        # setting the end date to the present date if user returns the item before the return date
        returntool.end_date = date.today()
        print(date.today())
        returntool.save()
    except(KeyError):
        borrowedtools = Sharedtool.objects.filter(Borrower=user, status='Borrowed')
        no_notification = max(numnotify(request) - user.seen, 0)
        context = {
            'borrowedtools': borrowedtools,
            'no_notification':no_notification
        }
        return render(request, 'borroweditems.html', context)
    else:

        return HttpResponseRedirect('/borroweditems/')


def notification(request):
    user = is_logged_in(request)
    if not user:
        return HttpResponseRedirect("/login/")

    borrowrequest_tool = Sharedtool.objects.filter(status='BorrowRequest', atool__Share_location='H', atool__Owner=user)
    returnrequest_tool = Sharedtool.objects.filter(status='ReturnRequest', atool__Share_location='H', atool__Owner=user)
    deniedrequest_tool = Sharedtool.objects.filter(status='Declined', Borrower_id=user)
    acknowledge_request = Sharedtool.objects.filter(status='Returned', Borrower_id=user)
    approvedrequest_tool = Sharedtool.objects.filter(status='Borrowed', Borrower_id=user)

    user.seen = borrowrequest_tool.count() + returnrequest_tool.count() + deniedrequest_tool.count() + acknowledge_request.count() + approvedrequest_tool.count()
    user.save()
    print("Inside notificaiton method, user is")
    print(user)
    print("usrseen is")
    print(user.seen)
    context = {
        'borrowrequest_tool': borrowrequest_tool,
        'returnrequest_tool': returnrequest_tool,
        'deniedrequest_tool': deniedrequest_tool,
        'acknowledge_request': acknowledge_request,
        'approvedrequest_tool': approvedrequest_tool
    }
    return render(request, 'notification.html', context)

def numnotify(request):
    user = is_logged_in(request)
    if not user:
        return HttpResponseRedirect("/login/")
    borrowrequest_tool = Sharedtool.objects.filter(status='BorrowRequest', atool__Share_location='H', atool__Owner=user)
    returnrequest_tool = Sharedtool.objects.filter(status='ReturnRequest', atool__Share_location='H', atool__Owner=user)
    deniedrequest_tool = Sharedtool.objects.filter(status='Declined', Borrower_id=user)
    acknowledge_request = Sharedtool.objects.filter(status='Returned', Borrower_id=user)
    approvedrequest_tool = Sharedtool.objects.filter(status='Borrowed', Borrower_id=user)

    num=borrowrequest_tool.count()+returnrequest_tool.count()+deniedrequest_tool.count()+acknowledge_request.count()+approvedrequest_tool.count()
    return(num)

def approve(request):
    user = is_logged_in(request)
    if not user:
        return HttpResponseRedirect("/login/")
    try:
        toolid = request.POST['tool_id']
        toolrowid = request.POST['id']
        approvetool = Sharedtool.objects.get(atool_id=toolid, id=toolrowid)
        if request.POST['button'] == 'Decline':
            print("declined message")
            approvetool.status = 'Declined'
            approvetool.owner_message = request.POST['message']
        elif request.POST['button'] == 'Approve':
            approvetool.status = 'Borrowed'
        else:
            approvetool.status = 'Returned'
        approvetool.save()
    except(KeyError):
        tools = Sharedtool.objects.filter(atool__Owner=user, status='BorrowRequest', atool__Share_location='H')
        returntools = Sharedtool.objects.filter(atool__Owner=user, status='ReturnRequest', atool__Share_location='H')
        no_notification = max(numnotify(request) - user.seen, 0)
        context = {
            'tools': tools,
            'returntools': returntools,
            'no_notification':no_notification
        }
        return render(request, 'approve.html', context)
    else:
        return HttpResponseRedirect('/approve/')


def othersheds(request):
    user = is_logged_in(request)
    if not user:
        return HttpResponseRedirect("/login/")

    user_shed = CommunityShed.objects.get(ShedZip=user.ZIP_Code)
    all_tools = Tool.objects.filter(Is_active=True).exclude(shed=user_shed)
    no_notification = max(numnotify(request) - user.seen, 0)
    context = {
        'all_tools': all_tools,
        'no_notification': no_notification
    }
    return render(request, 'othersheds.html', context)

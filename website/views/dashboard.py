from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from website.views.login import is_logged_in
from website.views.community import numnotify
from website import forms, models

from website.models.users import User
from website.models.tools import CommunityShed
from website.views.statistics import get_tool_stsstic, get_borrower_stsstic,get_lender_stsstic

def dashboard(request):
    user = is_logged_in(request)
    shed = CommunityShed.objects.get(ShedZip=user.ZIP_Code)
    print("User is" )
    print(user)
    if not user:
        return HttpResponseRedirect("/login/")
    no_notification = max(numnotify(request) - user.seen, 0)
    print( "no_notification" )
    print(no_notification)
    print( "userseen is")
    print(user.seen)

    finaltool = get_tool_stsstic()
    finalborrower = get_borrower_stsstic()
    finallender = get_lender_stsstic()


    dash_context = {
        'username': user.Email,
        'shed': shed,
        'no_notification':no_notification,
        'finaltool': sorted(finaltool.values(), reverse=True),
        'finalborrower': sorted(finalborrower.values()),
        'finallender': sorted(finallender.values(), reverse=True),
    }
    return render(request, 'dashboard.html', dash_context)

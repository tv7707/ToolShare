import operator

from django.shortcuts import render
from django.http import HttpResponseRedirect
from website.models.tools import Sharedtool,Tool
from website.views.login import is_logged_in
from website.models.users import User
from website.views.community import numnotify

def toolstatistics(request):
    user = is_logged_in(request)
    if not user:
        return HttpResponseRedirect("/login/")
        # return HttpResponse('This is community shed page.')

    no_notification = max(numnotify(request) - user.seen, 0)
    finaltool= get_tool_stsstic()
    finalborrower = get_borrower_stsstic()
    finallender = get_lender_stsstic()

    context = {
        'finaltool': sorted(finaltool.values(), reverse=True),
        'finalborrower': sorted(finalborrower.values()),
        'finallender': sorted(finallender.values(), reverse=True),
        'no_notification': no_notification
    }
    return render(request, 'statistics.html', context)

##################################### TOOOOOOOOOOL ##########################################

def get_tool_stsstic():
    tool_count = {}
    finaltool = {}
    for tool in Tool.objects.all():
        print(tool.Tool_Name)
        tool_count[tool] = get_used_count(tool)
        print(str(tool_count[tool]))
        finaltool[tool_count[tool]] = tool.Tool_Name + ' was used: (' + str(tool_count[tool]) + ') times. '
    print('----')
    print(finaltool)
    all_objects = sorted(tool_count.items(), key=operator.itemgetter(1), reverse=True)
    #final = sorted(final.items(), key=operator.itemgetter(1), reverse=True)
    print('=============================')
    print(finaltool)

    #all_objects = Sharedtool.objects.all()
    print(tool_count.values())
    return(finaltool)
def get_used_count(tool):
    return len(Sharedtool.objects.filter(atool = tool))


##################################### BORROWER ##########################################

def get_borrower_stsstic():
    borrower_count = {}
    finalBorrower = {}
    for borrower in User.objects.all():
        print('++++++++++++++++++++++++++++++++++++++++++++++')
        print(borrower.First_Name)
        borrower_count[borrower] = get_borrower_count(borrower)
        print(str(borrower_count[borrower]))
        finalBorrower[borrower_count[borrower]] = borrower.First_Name + ' borrowed: (' + str(borrower_count[borrower]) + ') tools. '
        print('++++++++++++++++++++++++++++++++++++++++++++++')
    print('----')
    print(finalBorrower)
    all_objects = sorted(borrower_count.items(), key=operator.itemgetter(1), reverse=True)
    #final = sorted(final.items(), key=operator.itemgetter(1), reverse=True)
    print('=============================')
    print(finalBorrower)

    #all_objects = Sharedtool.objects.all()
    print(borrower_count.values())
    return(finalBorrower)
def get_borrower_count(borrower):
    return len(Sharedtool.objects.filter(Borrower = borrower))

##################################### LENDER ##########################################
def get_lender_stsstic():
    lender_count = {}
    finallender = {}
    for lender in User.objects.all():
        print('++++++++++++++++++++++++++++++++++++++++++++++')
        print(lender.First_Name)
        lender_count[lender] = get_lender_count(lender)
        print(str(lender_count[lender]))
        finallender[lender_count[lender]] = lender.First_Name + ' shared: (' + str(lender_count[lender]) + ') tools. '
        print('++++++++++++++++++++++++++++++++++++++++++++++')
    print('----')
    print(finallender)
    all_objects = sorted(lender_count.items(), key=operator.itemgetter(1), reverse=True)
    #final = sorted(final.items(), key=operator.itemgetter(1), reverse=True)
    print('=============================')
    print(finallender)

    #all_objects = Sharedtool.objects.all()
    print(lender_count.values())
    return(finallender)

def get_lender_count(lender):
    return len(Sharedtool.objects.filter(atool__Owner = lender))

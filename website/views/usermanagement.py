from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic

from website import forms, models

from website.models.users import User

def usermanagement(request):
    page_context = {}
    return render(request, 'usermanagement.html', page_context)
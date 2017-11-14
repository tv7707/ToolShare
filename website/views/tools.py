from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic

from website import forms, models

from website.models.tools import Tool

def register(request):
    registration_form = forms.Registration(request.POST, request.FILES)

    if registration_form.is_valid():

        mytool = Tool()
        mytool.description = registration_form.cleaned_data['description']
        mytool.color = registration_form.cleaned_data['color']
        mytool.identifier = registration_form.cleaned_data['identifier']
        mytool.is_active = registration_form.cleaned_data['is_active']
        mytool.pickup_arrangements = registration_form.cleaned_data['pickup_arrangements']
        mytool.share_location_type = registration_form.cleaned_data['share_location_type']
        mytool.share_location = registration_form.cleaned_data['share_location']
        mytool.picture = request.FILES['picture']

        mytool.save()

        return HttpResponseRedirect('/dashboard')

    reg_context = {
        'reg_form': registration_form,
    }

    return render(request, 'tools.html', reg_context)
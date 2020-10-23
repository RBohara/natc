from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Membership

# Create your views here.


def membership(request):
    return render(request, 'membership/membership.html')


def uploadMembershipForm(request):
    if request.method == 'POST':
        title = "Request for Membership form"
        filled_form = request.FILES['membership_form']
        membership = Membership(title=title, filled_form=filled_form)
        membership.save()

        messages.success(request, 'Thank you for applying for membership!!!')
    return redirect('/membership')

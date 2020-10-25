from django.core.mail import EmailMessage, send_mail
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

        # subject = "Request for Membership"
        # sender = "natcbnetest@gmail.com"
        # message = "Please find the filled form for the membership"

        # email = EmailMessage(subject, message, sender, [
        #                      'rahul.bohara2016@gmail.com'])
        # email.attach(filled_form.name, filled_form.read(),
        #              filled_form.content_type)

        # email.send()

        messages.success(request, 'Thank you for applying for membership!!!')
    return redirect('/membership')

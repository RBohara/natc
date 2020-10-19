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
        # constructing an email
        # subject = "Membership Form"
        # text_content = "Please find the attached membership form"
        # from_email = "rahul.bohara2016@gmail.com"
        # to = "rahul.bohara2018@gmail.com"
        # email = EmailMessage(subject, text_content, from_email, [to])
        # email.attach_file(filled_form)
        # email.send()
        # messages.success(
        #     "Your membership form has been submitted. The team will get back to you as soon as possible"
        # )

    return redirect('/membership')

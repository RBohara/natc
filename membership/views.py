from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Membership

# from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent.parent


def membership(request):
    return render(request, 'membership/membership.html')


def uploadMembershipForm(request):
    if request.method == 'POST':
        family_name = request.POST['family_name']
        first_name = request.POST['first_name']
        name1 = request.POST['name1']
        name2 = request.POST['name1']
        name3 = request.POST['name1']
        relation1 = request.POST['relation1']
        relation2 = request.POST['relation2']
        relation3 = request.POST['relation3']
        unit = request.POST['unit']
        street_no = request.POST['street_no']
        street_name = request.POST['street_name']
        suburb = request.POST['suburb']
        state = request.POST['state']
        phone = request.POST['phone']
        email = request.POST['email']
        membership_type = request.POST['membership_type']
        receipt = request.POST['receipt']

        membership = Membership(
            family_name=family_name,
            first_name=first_name,
            name1=name1,
            name2=name2,
            name3=name3,
            relation1=relation1,
            relation2=relation2,
            relation3=relation3,
            unit=unit,
            street_no=street_no,
            street_name=street_name,
            suburb=suburb,
            state=state,
            membership_type=membership_type,
            phone=phone,
            email=email,
            receipt=receipt
        )

        membership.save()

        messages.success(request, 'Thank you for applying for membership!!!')

        # message = f"{first_name} {family_name} has applied for {membership_type} membership. \nThe bank transfer receipt number is {receipt}. Please login to admin panel for more details!!!"
        # send_mail(
        #     "Application for membership",
        #     message,
        #     'natcbnetest@gmail.com',
        #     ['natcbne@gmail.com', 'contact@natcbne.org']
        # )

    return redirect('/')

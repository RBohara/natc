from django.contrib import admin
from .models import Membership


class MembershipAdmin(admin.ModelAdmin):
    list_display = ('family_name', 'first_name', 'unit', 'street_no', 'street_name',
                    'suburb', 'state', 'membership_type', 'phone', 'email', 'receipt')
    list_filter = ('family_name', 'first_name', 'receipt', 'membership_type')


admin.site.register(Membership, MembershipAdmin)

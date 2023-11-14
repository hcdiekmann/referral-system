from django.contrib import admin
from .models import Person, Referral

# Custom admin classes for the admin interface
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'date_of_birth')

class ReferralAdmin(admin.ModelAdmin):
    list_display = ('person', 'referral_date', 'referrer_name')
    list_filter = ('referral_date',)  # example of filtering options

# Register your models here
admin.site.register(Person, PersonAdmin)
admin.site.register(Referral, ReferralAdmin)
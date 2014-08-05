from django.contrib import admin
from requests.models import PhotographerRequest

class PhotographerRequestAdmin(admin.ModelAdmin):
    fieldsets = (
        ('User Info', {
            'fields': (('first_name', 'last_name'), 'email', 'city', 'phone', 'organization', ('max_price', 'date_needed'), 'message'),
            'classes': ('wide', 'extrapretty'),
        }),
        ('Admin Info', {
            'fields': ('follow_up', 'fulfilled', 'payment_received', 'payment_made', 'notes'),
            'classes': ('wide', 'extrapretty'),
        }),
    )
    list_display = ('full_name', 'city', 'organization', 'max_price', 'date_needed', 'follow_up', 'fulfilled', 'payment_received', 'payment_made')
    list_filter = ('follow_up', 'fulfilled', 'payment_received', 'payment_made')
    
    def full_name(self, obj):
        return ("%s %s" % (obj.first_name, obj.last_name))
    
admin.site.register(PhotographerRequest, PhotographerRequestAdmin)
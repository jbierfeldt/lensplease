from django.contrib import admin
from photographer.models import PhotographerProfile

class PhotographerProfileAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(PhotographerProfile, PhotographerProfileAdmin)
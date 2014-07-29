from django.contrib import admin
from requests.models import PhotographerRequest

class PhotographerRequestAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(PhotographerRequest, PhotographerRequestAdmin)
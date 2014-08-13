from django.contrib import admin
from photos.models import PortfolioPhoto

class PortfolioPhotoAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(PortfolioPhoto, PortfolioPhotoAdmin)

# Register your models here.

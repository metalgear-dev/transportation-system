from django.contrib import admin
from .models import Area, Provider

# Register your models here.
admin.site.register(Provider, admin.ModelAdmin)
admin.site.register(Area, admin.ModelAdmin)

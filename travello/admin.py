from django.contrib import admin
from .models import Destination, registration

class Uregistration(admin.ModelAdmin):
    list_display = ('name','add','email','phone',)
    search_fields = ['name']
admin.site.register(Destination)
admin.site.register(registration, Uregistration)

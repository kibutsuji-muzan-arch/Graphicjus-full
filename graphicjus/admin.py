from django.contrib import admin
from .models import Contact, Services
# Register your models here.

admin.site.register(Services)
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    fields = ['name','email','contacted', 'service']
    list_display = ['uuid', 'contacted']
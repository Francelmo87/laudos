from django.contrib import admin
from .models import Client

# Register your models here.


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    search_fields = ['id', 'user', 'protocol', 'name', 'number']
    list_display = ['id', 'user', 'protocol', 'name', 'number', 'pdf', 'active']



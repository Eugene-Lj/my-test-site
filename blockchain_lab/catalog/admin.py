from django.contrib import admin
from .models import Table

class TableAdmin(admin.ModelAdmin):
    pass

admin.site.register(Table, TableAdmin)
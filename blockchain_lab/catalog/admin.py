from django.contrib import admin
from .models import Table
from .forms import TableForm

class TableAdmin(admin.ModelAdmin):
    pass

admin.site.register(Table, TableAdmin)

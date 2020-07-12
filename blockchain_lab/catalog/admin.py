from django.contrib import admin
from .models import Procurement


class ProcurementAdmin(admin.ModelAdmin):
    pass

admin.site.register(Procurement, ProcurementAdmin)

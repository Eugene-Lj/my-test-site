from django.contrib import admin
from .models import SERVICES, About, Portfolio, Team

#admin.site.register(SERVICES)
# Define the admin class
class SERVICESAdmin(admin.ModelAdmin):
    pass

# Register the admin class with the associated model
admin.site.register(SERVICES, SERVICESAdmin)

class AboutAdmin(admin.ModelAdmin):
    pass

# Register the admin class with the associated model
admin.site.register(About, AboutAdmin)

class PortfolioAdmin(admin.ModelAdmin):
    pass

# Register the admin class with the associated model
admin.site.register(Portfolio, PortfolioAdmin)

class TeamAdmin(admin.ModelAdmin):
    pass

# Register the admin class with the associated model
admin.site.register(Team, TeamAdmin)
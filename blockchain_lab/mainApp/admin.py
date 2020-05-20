from django.contrib import admin
from .models import Posts

#admin.site.register(Posts)
# Define the admin class
class PostsAdmin(admin.ModelAdmin):
    pass

# Register the admin class with the associated model
admin.site.register(Posts, PostsAdmin)
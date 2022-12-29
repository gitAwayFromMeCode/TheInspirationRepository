from django.contrib import admin
from .models import Quote

# Register your models here.
admin.site.register(Quote) # quotes can now be created from the admin GUI

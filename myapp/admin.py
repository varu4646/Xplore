from django.contrib import admin

# Register your models here.
from .models import Blog

# Register the Blog model with the admin interface
admin.site.register(Blog)
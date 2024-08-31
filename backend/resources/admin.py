from django.contrib import admin
from .models import Resource, UserResource


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('name', )

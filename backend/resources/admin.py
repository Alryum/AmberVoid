from django.contrib import admin
from .models import Resource, UserResource, UniqueItem, UserUniqueItem


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(UniqueItem)
class UniqueItemAdmin(admin.ModelAdmin):
    list_display = ('name',)

from django.contrib import admin
from .models import (
    Roles
)

# Register your models here.
@admin.register(Roles)
class RolesAdmin(admin.ModelAdmin):
    list_display = ['id','category']
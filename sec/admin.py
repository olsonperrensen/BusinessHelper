from django.contrib import admin
from .models import User
# Register your models here.

# ALLOW INHERITANCE OF THE BASE USER CLASS
@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name",
                    "email", "manager", "department")

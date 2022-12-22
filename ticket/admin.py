from django.contrib import admin
from .models import Ticket
# Register your models here.

# ALLOW /admin TO MODIFY TICKETS
admin.site.register(Ticket)

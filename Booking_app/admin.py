from django.contrib import admin
from .models import Booking, Contact, Room

# Register your models here.

admin.site.register(Contact)
admin.site.register(Room)
admin.site.register(Booking)
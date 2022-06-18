from django.contrib import admin
from .models import Customer, Customer_Room,RoomManager

# Register your models here.
admin.site.register(Customer)
admin.site.register(RoomManager)
admin.site.register(Customer_Room)
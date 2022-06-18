from django.db import models
from Customer_app.models import RoomManager,Customer

# Create your models here.
class Contact(models.Model):
    occuppant_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    occupant_job = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)
    def _str__(self):
     return "occuppant_name: "+self.occuppant_name
  

class Room(models.Model):
    manager = models.ForeignKey(RoomManager,on_delete=models.CASCADE)
    room_no = models.CharField(max_length=5, )
    user_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    room_type = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)
    price = models.FloatField(default=1000.00)
    no_of_night = models.IntegerField()
    start_date = models.DateField(auto_now=False,auto_now_add=False)
    end_day = models.DateField(auto_now=False, auto_now_add=False)
    amount_paid = models.IntegerField() 
    def __str__(self):
     return "room_no:  "+str(self.user_id)

class Booking(models.Model):
     room_no = models.ForeignKey(Room,on_delete=models.CASCADE)
     user_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
     start_day =models.DateField(auto_now =False,auto_now_add=False)
     end_day = models.DateField(auto_now=False,auto_now_add=False)
     amount = models.FloatField()
     booked_on = models.DateField(auto_now=True, auto_now_add=False)
     def __str__(self):
        return "Booking ID: "+str( self.user_id)
    
     
     

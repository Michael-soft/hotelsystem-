from django.db import models

# Create your models here.

class Customer(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    phone_no = models.CharField(max_length=50)
    def _str__(self):
       return "Customer:  "+self.username 

class RoomManager(models.Model):
    user_name = models.CharField(max_length=100)
    pass_word = models.CharField(max_length=100)
    manager_email = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=50)
    manager_gender = models.CharField(max_length=20)
    def __str__(self):
        return "Room Manager:  "+self.user_name 

class Customer_Room(models.Model):
     room_number = models.CharField(max_length=5)
     room_price = models.FloatField(default=1000.0)
     type_room = models.CharField(max_length=50)
     number_of_days = models.IntegerField()
     def __str__(self):
         return "room_number: "+str(self)
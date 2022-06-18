from django.db import models  

#Create your models here.

class Booking(models.Model):
    room_number = models.IntegerField()
    amount_paid =models.DecimalField(max_digits=10,decimal_places=2)
    occupant_name =models.CharField(max_length=100,null=False,help_text="your name,surname first")
    occupant_email = models.EmailField()
    occupant_occupation =models.CharField(max_length=100)
    number_of_night = models.IntegerField()
    start_date = models.DateTimeField()
    end_date =   models.DateTimeField()

    def __str__(self):
        return self.occupant_name

     
     

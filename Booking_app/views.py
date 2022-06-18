from datetime import datetime
from urllib import request
from django.shortcuts import render

from Customer_app.models import RoomManager
from .models import Contact,Room,Booking

# Create your views here

def index(request):
    return render(request, 'Booking/index.html',{})
def Contact(request):
    if request.method=="GET":   
     return render(request, "Contact/contact.html",{})
     occuppant_name=request.POST['name']
     email=request.POST ['email']
     message=request.POST ['message']
     data=Contact(name=occuppant_name,email=email,message=message)
     data.save()
     return render(request,"contact/contact.html")

def Booking(request):
    if request.method=="POST":
     start_day=request.POST['start_day']
     end_day=request.POST['end_day']
     request.session['start_day']=start_day
     request.session['end_day']=end_day
     start_day=datetime.datetime.strptime(start_day,"%d/%b/%Y").date()
     end_day=datetime.datetime.strptime(end_day,"%d/%b/%Y").date()
     data=Room.objects.filter(is_available=True,no_of_night=no_of_nights,start_day=start-day)
     request.session['no_of_night']=no_of_night
     return render(request,'Booking/Booking.html')
     
     
def booked_on(request,id):
     if request.session.get('user_id')
      request.session.get("room_type",None)=="Customer":
     if request.session.get("no_of_night",1):
      no_of_night=request.session['no_of_night']
      start_day=request.session['start_day']
      end_day=request.session['end_day']
      request.session['room_no']=id
      data=Room.objects.get(room_no=id)
      amount=data.price*int(no_of_night)
      request.session['amount']=amount
      RoomManager=data.manager.username 
      return render(request,"Booking/booking.html")













































































































































































def booked_on(request,id):
      
     
     








    


from django.shortcuts import render,redirect
from Booking_app.models import Booking
from .models import Customer_Room

# Create your views here.
def Customer_Room(request):
    if request.session.get('username',None) and 
    request.session.get('type',None)=='manager':
    return redirect ('Customer_Room')
    if request.session.get('username',None) and 
    request.session.get('type',None)=='Customer_Room':
    username=request.session['username']
    data=Customer_Room.objects.get(username=username)
    Booking=Booking.objects.filter(user_id=data).order_by('-id')
    available=len(booking_data)
    return render(request,"Customer_Room/index.html")
def details(request,id,booking):
    if not request.session.get('username',None):
     return redirect('RoomManager_login')
    if request.session.get('username',None) and request.session.get('type',None)=='customer':
      return redirect('user_dashboard')




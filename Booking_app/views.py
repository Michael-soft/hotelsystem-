from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import Booking

#This is the views that was created for the program

def Manager(request):
    if request.method == "POST":
        user_data = UserCreationForm(request.POST)
        if user_data.is_valid():
            user_data.save()
            return redirect("Booking:loginview")
        else:
            pass
        context ={  
            "form": UserCreationForm()
        }
        return render(request, "Booking/manager.html",context)

def User(request):
    if request.method =="POST":
        customer_name  = request.POST.get('customer_name')
        customer_email = request.POST.get('customer_email')
        customer_work  = request.POST.get('customer_work')
        amount_paid   = request.POST.get('amount_paid')
        room_number   = request.POST.get('room_number')
        duration      = request.POST.get('duration')
        check_in      = request.POST.get('check_in')
        check_out     = request.POST.get('check_out')


        new_customer = Booking(room_number=room_number,
                               amount_paid=amount_paid,
                               ocuppant_name=customer_name,
                               ocuppant_email=customer_email,
                               ocuppant_occupation=customer_work,
                               number_of_night=duration,
                               start_date=check_in,
                               end_date=check_out,
                               )

        new_customer.save()
        return redirect('Booking: portalview')

    return render(request,"Booking/User.html")

def login(request):
    return redirect("Booking:userview")

def Portal(request):
    return render(request,"Booking/portal.html")
















































































 
     
     








    


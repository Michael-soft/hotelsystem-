from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('Contact',views.Contact/Contact.html,name='Contact'),
    path('Booking',views.Booking/Booking,name='Booking'),
    Path('booked_on/<str:id>',views.booked_on,name='booked_on'),
]

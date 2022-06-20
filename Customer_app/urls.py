from django.urls import path
from .views import Customer,Contact



app_name = "Customer_app"

urlpatterns = [                                
    path(" ", Customer, name = "Contactview"),
    path("Contact", Contact, name = "Contactview"),
]


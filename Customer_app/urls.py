from django.urls import path
from .views import Customer,Contact



app_name = "Customer_app"

urlpatterns = [                                
    path("", Customer, name = "Contactcview"),
    path("Contact", Contact, name = "contactview"),
]


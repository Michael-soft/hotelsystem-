from django.urls import path
from .views import Manager, User, Portal, login
from django.contrib.auth import views as auth_views

app_name = "Booking"

urlpatterns = [
    path("", Portal, name = "portalview"),
    path("login/", auth_views.LoginView.as_view(template_name="Booking/login.html"), name = "loginview"),
    path("Manager", Manager, name = "Managerview"),
    path("User", User, name = "Userview"),
    path("logout/", auth_views.LogoutView.as_view(template_name="Booking/logout.html"), name = "logoutview")
    
]

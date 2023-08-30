from pathlib import Path
from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeVista.as_view(), name="home"),
    path('login',views.LoginVista.as_view(), name="login"),
    path('logout',views.logoutUser, name="logout"),
    
    # Template Authentication Views
    # path("accounts/", include("django.contrib.auth.urls")),
]
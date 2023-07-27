from pathlib import Path
from django.urls import path
from . import views

urlpatterns = [
    # path('',views.HomeVista.as_view(), name="home"),
    path('login_user',views.login_user, name="login"),
    path('login_user2',views.LoginVista.as_view(), name="login2"),
    
]
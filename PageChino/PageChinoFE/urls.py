from pathlib import Path
from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeVista.as_view(), name="home"),
]
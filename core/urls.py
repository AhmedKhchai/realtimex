# core/urls.py
from django.urls import path, include
from core import views

app_name = "core"  

urlpatterns = [
    path("", views.data_sources, name="data_sources"),
    path("alphavantage/", views.alphavantage, name="alphavantage"),
]

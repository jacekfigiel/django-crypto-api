from django.urls import path
from . import views

app_name = "coin_app"

urlpatterns = [
    path("home/", views.home, name="home_view")
]

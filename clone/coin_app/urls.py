from django.urls import path
from .views import home, CryptoDetailView

app_name = "coin_app"

urlpatterns = [
    path("home/", home, name="home_view"),
    path("detail_crypto/<int:pk>", CryptoDetailView.as_view(), name="detail_view")
]

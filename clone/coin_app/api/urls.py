from django.urls import path
from .views import home, CryptoDetailView, home_price, home_symbol, home_percent_change_24h, home_percent_change_7d, home_market_cap, home_volume_24h, home_circulating_supply, search

app_name = "coin_app"

urlpatterns = [
    path("home/", home, name="home_view"),
    path("home_price/", home_price, name="home_view_price"),
    path("home_symbol/", home_symbol, name="home_view_symbol"),
    path("home_percent_change_24h/", home_percent_change_24h, name="home_percent_change_24h"),
    path("home_percent_change_7d/", home_percent_change_7d, name="home_percent_change_7d"),
    path("home_market_cap/", home_market_cap, name="home_market_cap"),
    path("home_volume_24h/", home_volume_24h, name="home_volume_24h"),
    path("home_circulating_supply/", home_circulating_supply, name="home_circulating_supply"),
    path("detail_crypto/<int:pk>", CryptoDetailView.as_view(), name="detail_view"),
    path("search/", search, name='search_result')
]

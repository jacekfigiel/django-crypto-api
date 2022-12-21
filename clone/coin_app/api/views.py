from django.shortcuts import render, redirect
from django.views.generic import DetailView
from ..models import CryptoModel
# Create your views here.


def home(request):
    crypto_list = CryptoModel.objects.order_by("name")
    crypto_dict = {"access_crypto": crypto_list}
    return render(request, "coin_app/home.html", context=crypto_dict)

def home_symbol(request):
    crypto_list = CryptoModel.objects.order_by("symbol")
    crypto_dict = {"access_crypto": crypto_list}
    return render(request, "coin_app/home.html", context=crypto_dict)

def home_price(request):
    crypto_list = CryptoModel.objects.order_by("-price")
    crypto_dict = {"access_crypto": crypto_list}
    return render(request, "coin_app/home.html", context=crypto_dict)

def home_percent_change_24h(request):
    crypto_list = CryptoModel.objects.order_by("-percent_change_24h")
    crypto_dict = {"access_crypto": crypto_list}
    return render(request, "coin_app/home.html", context=crypto_dict)

def home_percent_change_7d(request):
    crypto_list = CryptoModel.objects.order_by("-percent_change_7d")
    crypto_dict = {"access_crypto": crypto_list}
    return render(request, "coin_app/home.html", context=crypto_dict)

def home_market_cap(request):
    crypto_list = CryptoModel.objects.order_by("-market_cap")
    crypto_dict = {"access_crypto": crypto_list}
    return render(request, "coin_app/home.html", context=crypto_dict)

def home_volume_24h(request):
    crypto_list = CryptoModel.objects.order_by("-volume_24h")
    crypto_dict = {"access_crypto": crypto_list}
    return render(request, "coin_app/home.html", context=crypto_dict)

def home_circulating_supply(request):
    crypto_list = CryptoModel.objects.order_by("-circulating_supply")
    crypto_dict = {"access_crypto": crypto_list}
    return render(request, "coin_app/home.html", context=crypto_dict)

class CryptoDetailView(DetailView):
    context_object_name = "crypto_model"
    model = CryptoModel

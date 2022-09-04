from django.shortcuts import render
from .models import CryptoModel
# Create your views here.


def home(request):
    crypto_list = CryptoModel.objects.order_by("name")
    crypto_dict = {"access_crypto": crypto_list}
    return render(request, "coin_app/home.html", context=crypto_dict)
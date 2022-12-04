from django import forms
from .models import CryptoModel


class CryptoSearch(forms.Form):
    search_crypto = forms.CharField(label="crypto_name")

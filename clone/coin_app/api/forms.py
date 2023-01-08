from django import forms
from ..models import CryptoModel


class SearchForm(forms.Form):
   q = forms.CharField(label = 'Search', max_length=50)
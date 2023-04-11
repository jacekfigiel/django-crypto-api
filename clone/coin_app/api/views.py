from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from ..models import CryptoModel, PreciousMetalsModel, NewsModel


# Create your views here.

def search(request):
    search_query = ''
    if request.GET.get('q'):
        search_query = request.GET.get('q')
    else:
        search_query = ("No coin found")
    posts = CryptoModel.objects.filter(name__icontains=search_query, symbol__icontains=search_query)
    context = {'posts': posts, 'search_query': search_query}
    return render(request, 'coin_app/search.html', context)


def home(request):
    crypto_list = CryptoModel.objects.order_by("name")
    metal_list = PreciousMetalsModel.objects.order_by("rate")
    news_list = NewsModel.objects.order_by("-published")[:5]
    context = {
        "access_crypto": crypto_list,
        "access_metal": metal_list,
        "access_news": news_list
    }
    return render(request, "coin_app/home.html", context=context)


def home_symbol(request):
    crypto_list = CryptoModel.objects.order_by("symbol")
    metal_list = PreciousMetalsModel.objects.order_by("rate")
    context = {
        "access_crypto": crypto_list,
        "access_metal": metal_list
    }
    return render(request, "coin_app/home.html", context=context)


def home_price(request):
    crypto_list = CryptoModel.objects.order_by("-price")
    metal_list = PreciousMetalsModel.objects.order_by("rate")
    context = {
        "access_crypto": crypto_list,
        "access_metal": metal_list
    }
    return render(request, "coin_app/home.html", context=context)


def home_percent_change_24h(request):
    crypto_list = CryptoModel.objects.order_by("-percent_change_24h")
    metal_list = PreciousMetalsModel.objects.order_by("rate")
    context = {
        "access_crypto": crypto_list,
        "access_metal": metal_list
    }
    return render(request, "coin_app/home.html", context=context)


def home_percent_change_7d(request):
    crypto_list = CryptoModel.objects.order_by("-percent_change_7d")
    metal_list = PreciousMetalsModel.objects.order_by("rate")
    context = {
        "access_crypto": crypto_list,
        "access_metal": metal_list
    }
    return render(request, "coin_app/home.html", context=context)


def home_market_cap(request):
    crypto_list = CryptoModel.objects.order_by("-market_cap")
    metal_list = PreciousMetalsModel.objects.order_by("rate")
    context = {
        "access_crypto": crypto_list,
        "access_metal": metal_list
    }
    return render(request, "coin_app/home.html", context=context)


def home_volume_24h(request):
    crypto_list = CryptoModel.objects.order_by("-volume_24h")
    metal_list = PreciousMetalsModel.objects.order_by("rate")
    context = {
        "access_crypto": crypto_list,
        "access_metal": metal_list
    }
    return render(request, "coin_app/home.html", context=context)


def home_circulating_supply(request):
    crypto_list = CryptoModel.objects.order_by("-circulating_supply")
    metal_list = PreciousMetalsModel.objects.order_by("rate")
    context = {
        "access_crypto": crypto_list,
        "access_metal": metal_list
    }
    return render(request, "coin_app/home.html", context=context)


class CryptoDetailView(DetailView):
    context_object_name = "crypto_model"
    model = CryptoModel


class PreciousMetalsListView(ListView):
    model = PreciousMetalsModel
    template_name = 'coin_app/precious_metals_list.html'
    context_object_name = 'metal_list'
    ordering = ['rate']


class NewsListView(ListView):
    model = NewsModel
    template_name = 'coin_app/news.html'
    context_object_name = "news_list"
    ordering = ['-published']

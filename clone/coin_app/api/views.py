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


def get_ordered_lists(order_by):
    crypto_list = CryptoModel.objects.order_by(order_by)
    metal_list = PreciousMetalsModel.objects.order_by("rate")
    news_list = NewsModel.objects.order_by("-published")[:5]
    context = {
        "access_crypto": crypto_list,
        "access_metal": metal_list,
        "access_news": news_list
    }
    return context


def home(request):
    context = get_ordered_lists("name")
    return render(request, "coin_app/home.html", context=context)


def home_symbol(request):
    context = get_ordered_lists("symbol")
    return render(request, "coin_app/home.html", context=context)


def home_price(request):
    context = get_ordered_lists("-price")
    return render(request, "coin_app/home.html", context=context)


def home_percent_change_24h(request):
    context = get_ordered_lists("-percent_change_24h")
    return render(request, "coin_app/home.html", context=context)


def home_percent_change_7d(request):
    context = get_ordered_lists("-percent_change_7d")
    return render(request, "coin_app/home.html", context=context)


def home_market_cap(request):
    context = get_ordered_lists("-market_cap")
    return render(request, "coin_app/home.html", context=context)


def home_volume_24h(request):
    context = get_ordered_lists("-volume_24h")
    return render(request, "coin_app/home.html", context=context)


def home_circulating_supply(request):
    context = get_ordered_lists("-circulating_supply")
    return render(request, "coin_app/home.html", context=context)


class CryptoDetailView(DetailView):
    context_object_name = "crypto_model"
    model = CryptoModel


def get_crypto_ordered_lists(order_by):
    crypto_list = CryptoModel.objects.order_by(order_by)
    context = {
        "crypto_list": crypto_list,
    }
    return context


class CryptoView(ListView):
    model = CryptoModel
    template_name = 'coin_app/crypto_list.html'
    context_object_name = 'crypto_list'
    ordering = ['market_cap']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order_by = self.request.GET.get('order_by', 'name')
        context.update(get_crypto_ordered_lists(order_by))
        return context


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

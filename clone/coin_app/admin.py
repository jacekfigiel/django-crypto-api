from django.contrib import admin
from .models import CryptoModel, PreciousMetalsModel, NewsModel
# Register your models here.

admin.site.register(CryptoModel)
admin.site.register(PreciousMetalsModel)
admin.site.register(NewsModel)

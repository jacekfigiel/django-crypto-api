from django.db import models

# Create your models here.


class CryptoModel(models.Model):
    name = models.TextField(max_length=100)
    symbol = models.TextField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    percent_change_24h = models.DecimalField(max_digits=20, decimal_places=2)
    percent_change_7d = models.DecimalField(max_digits=20, decimal_places=2)
    market_cap = models.IntegerField()
    volume_24h = models.IntegerField()
    circulating_supply = models.IntegerField()

    def __str__(self):
        return f"{self.symbol}, {self.name}, \n{self.price}$ " \
               f"\n{self.percent_change_24h}%, \n{self.percent_change_7d}% " \
               f"\n{self.market_cap}$, \n{self.volume_24h}$, \n{self.circulating_supply} {self.symbol}"


class PreciousMetalsModel(models.Model):
    code = models.TextField(max_length=20)
    rate = models.DecimalField(max_digits=20, decimal_places=10)

    def __str__(self):
        return f"{self.code}-{self.rate}"

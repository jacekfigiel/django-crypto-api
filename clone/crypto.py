import decimal


class Crypto:

    def __init__(self, name: str, symbol: str, price: int, percent_change_24h: int,
                 percent_change_7d: int, market_cap: int, volume_24h: int,
                 circulating_supply: int):
        self.name = name
        self.symbol = symbol
        self.price = price
        self.percent_change_24h = percent_change_24h
        self.percent_change_7d = percent_change_7d
        self.market_cap = market_cap
        self.volume_24h = volume_24h
        self.circulating_supply = circulating_supply

    def __str__(self):
        return f"{self.symbol}, {self.name}, \n{self.price}$ " \
               f"\n{self.percent_change_24h}%, \n{self.percent_change_7d}% " \
               f"\n{self.market_cap}$, \n{self.volume_24h}$, \n{self.circulating_supply} {self.symbol}"


class PreciousMetals:

    def __init__(self, code: str, rate: int):
        self.code = code
        self.rate = rate

    def __str__(self):
        return f"{self.code}" \
                f"\n{self.rate}"

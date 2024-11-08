from __future__ import annotations
from typing import Type


class Currency:
    """
    1 EUR = 2 USD = 100 GBP

    1 EUR = 2 USD    ;  1 EUR = 100 GBP
    1 USD = 0.5 EUR  ;  1 USD = 50 GBP
    1 GBP = 0.02 USD ;  1 GBP = 0.01 EUR
    """

    currency_code = None
    rates = {
        ('EUR', 'USD'): 2.0,
        ('EUR', 'GBP'): 100.0,
        ('USD', 'EUR'): 0.5,
        ('USD', 'GBP'): 50.0,
        ('GBP', 'EUR'): 0.01,
        ('GBP', 'USD'): 0.02,
        ('EUR', 'EUR'): 1.0,
        ('USD', 'USD'): 1.0,
        ('GBP', 'GBP'): 1.0
    }

    def __init__(self, value: float):
        self.value = value


    @classmethod
    def course(cls, other_cls: Type[Currency]) -> str:
        #raise NotImplementedError
        # {float value} {currency to} for 1 {currency for}
        rate = cls.rates[(cls.currency_code, other_cls.currency_code)]
        return f"{rate} {other_cls.currency_code} for 1 {cls.currency_code}"

    def to_currency(self, other_cls: Type[Currency]):
        #raise NotImplementedError
        rate = self.rates[(self.currency_code, other_cls.currency_code)]
        return other_cls(self.value * rate)

    def __add__(self, other:Currency):
        rate = Currency.rates[(other.currency_code, self.currency_code)]
        return self.__class__(self.value + other.value * rate)

    def __str__(self):
        return f"{self.value} {self.currency_code}"

class Euro(Currency):
    currency_code = 'EUR'


class Dollar(Currency):
    currency_code = 'USD'


class Pound(Currency):
    currency_code = 'GBP'


# Example usage
e = Euro(100)
r = Pound(100)
d = Dollar(200)

print(Euro.course(Pound))    # 100.0 GBP for 1 EUR
print(Dollar.course(Pound))  # 50.0 GBP for 1 USD
print(Pound.course(Euro))    # 0.01 EUR for 1 GBP

# Conversion examples
print(e.to_currency(Dollar)) # 200.0 USD
print(e.to_currency(Pound))  # 10000.0 GBP
print(r.to_currency(Euro))   # 1.0 EUR

# Addition examples
print(e + r)  # 101.0 EUR
print(r + d)  # 10100.0 GBP
print(d + e)  # 400.0 USD
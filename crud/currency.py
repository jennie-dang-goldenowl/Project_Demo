import requests
from django.conf import settings
from django.core.cache import cache
from djmoney.money import Money
from djmoney.contrib.exchange.models import convert_money

class CurrencyExchange:
    def get_rates_from_api(self, base_currency):
        url = f'{settings.CURRENCY_RATES_URL}?base={base_currency}'
        return requests.get(url).json()
    
    def get_key(self, base_currency):
        return f'currencies-{base_currency}'    

    def get_all_rates(self, base_currency):
        key = self.get_key(base_currency)
        return cache.get_or_set(key, lambda: self.get_rates_from_api(base_currency))

    def get_rate(self, base_currency, currency):
        return self.get_all_rates(base_currency)['rates'][currency]
      
    def get_converted_amount(self, amount, base_currency, converted_currency):
        return round(float(amount) * float(self.get_rate(base_currency.upper(), converted_currency.upper())), 3)

    def convert(self, money, currency):
        self.validate_money(money)
        amount = money.amount
        base_currency = str(money.currency)
        converted_currency = str(currency)
        convert_money(Money(money, 'USD'), 'VND')

        if base_currency.upper() == converted_currency.upper():
            return money
        return Money(self.get_converted_amount(amount, base_currency, converted_currency), converted_currency)

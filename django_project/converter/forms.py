from django import forms
import requests

currency_abbreviations = ['BGN', 'EUR', 'USD','CHF', 'GBP', 'CNY']

def convert_list(lst=list):
    tuple_list_of_curr = []
    for x in lst:
        tp = (x, x)
        tuple_list_of_curr.append(tp)
    return tuple_list_of_curr

"""def calculate_exchange(current_currency, desired_currency):
    API_KEY = '3B2IY9JPDHQ9IZDL'
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={current_currency}&to_currency={desired_currency}&apikey={API_KEY}'
    r = requests.get(url)
    data_dict = r.json()
    exchange_rate = float(data_dict['Realtime Currency Exchange Rate']['5. Exchange Rate'])
    return exchange_rate"""

class ConverterCurrency(forms.Form):
    current_currency = forms.ChoiceField(choices=convert_list(currency_abbreviations))
    amount = forms.CharField(max_length=100)
    desired_currency = forms.ChoiceField(choices=convert_list(currency_abbreviations))
from django import forms

currency_abbreviations = ['BGN', 'EUR', 'USD','CHF', 'GBP']

def convert_list(lst=list):
    """"Convert currency abbreviations into a list of tuples."""
    tuple_list_of_curr = []
    for x in lst:
        tp = (x, x)
        tuple_list_of_curr.append(tp)
    return tuple_list_of_curr

class ConverterCurrency(forms.Form):
    current_currency = forms.ChoiceField(choices=convert_list(currency_abbreviations))
    amount = forms.FloatField()
    desired_currency = forms.ChoiceField(choices=convert_list(currency_abbreviations))
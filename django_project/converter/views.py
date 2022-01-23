from django.shortcuts import render
from .forms import ConverterCurrency
from forex.models import RatesByPairsModel

def about(request):
    return render(request, 'converter/about.html')

def home(request):
    form = ConverterCurrency
    if request.method == "POST":
        amount = request.POST['amount']
        current_currency = request.POST['current_currency']
        desired_currency = request.POST['desired_currency']
        if current_currency == desired_currency:
            exchange_rate = 1
        else:
            result = RatesByPairsModel.objects.filter(pair=f'{current_currency}{desired_currency}').first()
            exchange_rate = result.exchange_rate
        result = f"{int(amount) * exchange_rate} {desired_currency}  {exchange_rate}"
        context = {
            'amount': amount,
            'current_currency': current_currency,
            'desired_currency': desired_currency,
            'result': result,
            'form': form
        }

        return render(request, 'converter/result.html', context)
    else:
        return render(request, 'converter/home.html', {'form': form})
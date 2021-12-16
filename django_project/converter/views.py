from django.shortcuts import render
from .forms import ConverterCurrency, calculate_exchange

def about(request):
    return render(request, 'converter/about.html')

def home(request):
    form = ConverterCurrency
    if request.method == "POST":
        amount = request.POST['amount']
        current_currency = request.POST['current_currency']
        desired_currency = request.POST['desired_currency']
        exchange_rate = calculate_exchange(current_currency, desired_currency)
        result = f"{int(amount) * exchange_rate} {desired_currency}"
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
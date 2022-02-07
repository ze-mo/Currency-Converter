from django.shortcuts import render
from .forms import ConverterCurrency
from forex.models import RatesByPairs
from users.models import RatesHistory
from datetime import datetime

def about(request):
    return render(request, 'converter/about.html', {'title': 'About'})

def home(request):
    """"Renders the home page, containing the converter and a conversion 
    history table if the current user is authenticated."""

    form = ConverterCurrency
    if request.method == "POST":
        amount = request.POST['amount']
        current_currency = request.POST['current_currency']
        desired_currency = request.POST['desired_currency']
        pair = f'{current_currency}{desired_currency}'
        if current_currency == desired_currency:
            exchange_rate = 1
        else:
            result = RatesByPairs.objects.filter(pair=pair).first()
            exchange_rate = result.exchange_rate
        float_result = float(amount) * exchange_rate
        formatted_exchange_rate = float("{:.4f}".format(exchange_rate))
        result = "{:.2f} {}".format(float_result, desired_currency)
        formatted_result = float("{:.2f}".format(float_result))

        if request.user.is_authenticated:
            p_id = request.user.profile.id
            conversion_date = datetime.now()
            history_record = RatesHistory.objects.create(profile_id=p_id, pair=pair, amount=amount, exchange_rate=formatted_exchange_rate, result=formatted_result, conversion_date=conversion_date)
            history_record.save()

        context = {
            'amount': amount,
            'current_currency': current_currency,
            'desired_currency': desired_currency,
            'result': result,
            'form': form
        }

        return render(request, 'converter/result.html', context)

    else:
        if request.user.is_authenticated:
            p_id = request.user.profile.id
            record_objects = RatesHistory.objects.filter(profile_id=p_id).defer('profile_id')[:5]
            records_list = []
            if record_objects:
                for object in record_objects:
                    object_dict = object.__dict__
                    del object_dict['_state']
                    del object_dict['id']
                    records_list.append(object_dict)
                return render(request, 'converter/home.html', {'form': form, 'records_list': records_list, 'object_dict': object_dict})
            else:
                return render(request, 'converter/home.html', {'form': form})

        return render(request, 'converter/home.html', {'form': form})


from django.shortcuts import render
from .forms import ConverterCurrency
from forex.models import RatesByPairsModel
from django.views.generic import ListView
from users.models import Profile
from users.models import RatesHistory
from datetime import datetime

def about(request):
    return render(request, 'converter/about.html')

def home(request):
    form = ConverterCurrency
    if request.method == "POST":
        amount = request.POST['amount']
        current_currency = request.POST['current_currency']
        desired_currency = request.POST['desired_currency']
        pair = f'{current_currency}{desired_currency}'
        if current_currency == desired_currency:
            exchange_rate = 1
        else:
            result = RatesByPairsModel.objects.filter(pair=pair).first()
            exchange_rate = result.exchange_rate
        float_result = float(amount) * exchange_rate
        result = "{:.2f} {}".format(float_result, desired_currency)

        if request.user.is_authenticated:
            p_id = request.user.profile.id
            conversion_date = datetime.now()
            history_record = RatesHistory.objects.create(profile_id=p_id, pair=pair, amount=amount, exchange_rate=exchange_rate, result=float_result, conversion_date=conversion_date)
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
            for object in record_objects:
                object_dict = object.__dict__
                del object_dict['_state']
                del object_dict['id']
                records_list.append(object_dict)
            return render(request, 'converter/home.html', {'form': form, 'records_list': records_list, 'object_dict': object_dict})

        return render(request, 'converter/home.html', {'form': form})

"""class RatesListView(ListView):
    user_model = RatesHistory
    template_name = 'converter/home.html'
    context_object_name = ''
    #user_model.searched
    #ordering = ['-date_posted']"""
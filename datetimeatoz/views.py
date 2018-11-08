from django.shortcuts import render
from django.http import HttpResponseRedirect


from .forms import PeriodBetweenDatesForm

# Create your views here.
class DateTimeViews:
    def __init__(self):
        pass

    def index(request):
        return render(request, 'datetimeatoz/index.html')

    def get_period_between_date_inputs(request):
        if request.method == 'POST':
            form = PeriodBetweenDatesForm(request.POST)
            if form.is_valid():
                return render(request, 'datetimeatoz/index.html', {'form': request.POST})
            else:
                return HttpResponseRedirect('/datetime_a_to_z/')


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
        if request.method == 'post':
            form = PeriodBetweenDatesForm(request.POST)
            if form.is_valid():
                return render(request, 'datetimeatoz/index.html', {'form': form})
            else:
                return HttpResponseRedirect('/')


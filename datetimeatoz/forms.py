from django import forms

class PeriodBetweenDatesForm(forms.Form):
    fromDate = forms.DateTimeField(label='From Date')
    toDate = forms.DateTimeField(label="To Date")

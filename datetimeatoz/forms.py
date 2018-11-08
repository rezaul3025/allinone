from django import forms

class PeriodBetweenDatesForm(forms.Form):
    fromDate = forms.DateTimeField(label='fromDate', required=True)
    toDate = forms.DateTimeField(label='toDate',required=True)

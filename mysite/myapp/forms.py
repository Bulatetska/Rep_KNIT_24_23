from django import forms

class CityForm(forms.Form):
    city = forms.CharField(label='Місто', max_length=100)

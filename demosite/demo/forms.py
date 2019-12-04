from django.forms import ModelForm
from .models import Rates, Comments
from django import forms

class RateListForm(ModelForm):
    rate_choice1 = forms.ChoiceField(choices=Rates.options, widget=forms.RadioSelect)
    rate_choice2 = forms.ChoiceField(choices=Rates.options, widget=forms.RadioSelect)
    rate_choice3 = forms.ChoiceField(choices=Rates.options, widget=forms.RadioSelect)
    rate_choice4 = forms.ChoiceField(choices=Rates.options, widget=forms.RadioSelect)
    rate_choice5 = forms.ChoiceField(choices=Rates.options, widget=forms.RadioSelect)

    class Meta:
        model = Rates
        fields = ('rate_choice1','rate_choice2','rate_choice3','rate_choice4','rate_choice5',)
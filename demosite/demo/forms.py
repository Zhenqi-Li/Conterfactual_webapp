from django.forms import ModelForm
from .models import Survey_rates
from django import forms

class RateListForm(ModelForm):
    rate_choice1 = forms.ChoiceField(choices=Survey_rates.options, widget=forms.RadioSelect)
    rate_choice2 = forms.ChoiceField(choices=Survey_rates.options, widget=forms.RadioSelect)
    rate_choice3 = forms.ChoiceField(choices=Survey_rates.options, widget=forms.RadioSelect)
    rate_choice4 = forms.ChoiceField(choices=Survey_rates.options, widget=forms.RadioSelect)
    rate_choice5 = forms.ChoiceField(choices=Survey_rates.options, widget=forms.RadioSelect)

    class Meta:
        model = Survey_rates
        fields = ('rate_choice1','rate_choice2','rate_choice3','rate_choice4','rate_choice5',)

class attentionform(forms.Form):
    options = (
        (True, ''),
        (False, ''),
    )
    choice1 = forms.ChoiceField(choices=options, widget=forms.RadioSelect)
    choice2 = forms.ChoiceField(choices=options, widget=forms.RadioSelect)

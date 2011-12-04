from django import forms
from realworldlike.models import PrintRun, Spot



class PrintRunForm(forms.ModelForm):
    #quantity = forms.ChoiceField(choices=[(x, x) for x in xrange(20)])
    class Meta:
        model = PrintRun


class SpotForm(forms.ModelForm):
    class Meta:
        model = Spot

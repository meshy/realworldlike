from django import forms
from realworldlike.models import Spot


class SpotForm(forms.ModelForm):
    class Meta:
        model = Spot

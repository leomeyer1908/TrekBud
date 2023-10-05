# travel/forms.py
from django import forms
from .models import TravelRegion

class RegionSelectionForm(forms.Form):
    region = forms.ModelChoiceField(
        queryset=TravelRegion.objects.all(),
        empty_label="Select a Region",
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

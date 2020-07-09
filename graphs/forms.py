from django import forms
from django.forms import inlineformset_factory
from django.forms.widgets import CheckboxSelectMultiple

from .models import GraphData

class GraphForm(forms.ModelForm):

    class Meta:
        model = GraphData
        fields = ('')

from django import forms
from .models import design


class DesignForm(forms.ModelForm):
    class Meta:
        model = design
        fields = ['name', 'rate', 'image']

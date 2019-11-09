from django import forms
from .models import Link


class LinkModelForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = [
            'full_url',
        ]
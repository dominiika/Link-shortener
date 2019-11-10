from django import forms
from .models import Link


class LinkModelForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = [
            'full_url',
        ]

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['full_url'].widget.attrs.update({'placeholder': 'https://your-url.com'})

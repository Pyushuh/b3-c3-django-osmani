# password_manager/forms.py
from django import forms
from .models import Site


class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['name', 'url', 'username', 'password']

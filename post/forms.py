from django import forms
from .models import EmailSubcribe

class EmailNews(forms.ModelForm):
    class Meta():
        model = EmailSubcribe
        fields = ['email']
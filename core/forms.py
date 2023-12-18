# forms.py

from django import forms

class CommandForm(forms.Form):
    command = forms.CharField(label='Enter your command')

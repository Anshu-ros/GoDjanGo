from django import forms
from django.utils import timezone

class studentpanel(forms.Form):
	r_date = forms.DateField(help_text="Enter a date.")
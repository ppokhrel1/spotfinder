from django import forms

from .models import Spot


class SpotForm(forms.ModelForm):
	class Meta:
		fields = ['report']
		model = Spot
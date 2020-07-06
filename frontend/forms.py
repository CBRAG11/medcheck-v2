from django import forms
from django.forms import ModelForm

from meds.models import User
from meds.models import Med

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class MedForm(forms.ModelForm):
    class Meta:
        model = Med
        fields = '__all__'
        

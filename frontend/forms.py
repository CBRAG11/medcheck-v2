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
        med_name = forms.CharField(label='med_name', widget=forms.TextInput(attrs={'placeholder': 'Enter Med Name'}))
        widgets = {
            'med_name': forms.TextInput(attrs={'placeholder': 'Enter medication name'}),
            'avg_dosage': forms.TextInput(attrs={'placeholder': 'Enter the dosage taken on average'}),
            'category': forms.TextInput(attrs={'placeholder': 'Enter drug category'}),
            
        }
        fields = '__all__'
        

from django import forms
from . import models


from django.core.validators import MaxValueValidator, MinValueValidator
# Create your forms here.
class Campus(forms.ModelForm): 
  class Meta:
    model = models.Campus
    fields = ('id', 'name', 'address', )
    widgets = {
      'id': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'placeholder': "Campus id",'autofocus': ''}),
      'name': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'placeholder': "Campus name",'autofocus': ''}),
      'address': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'placeholder': "Campus address",'autofocus': ''})
    }

class Campus_modify(forms.ModelForm):
  class Meta:
    model = models.Campus
    fields = ('name', 'address', )
    widgets = {
      'name': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'placeholder': "Campus name",'autofocus': ''}),
      'address': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'placeholder': "Campus address",'autofocus': ''})
    }
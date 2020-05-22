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

class Major(forms.ModelForm): 
  class Meta:
    model = models.Major
    fields = ('id', 'name', 'address', 'principal','campus',)
    widgets = {
      'id': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'placeholder': "Major id",'autofocus': ''}),
      'name': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'placeholder': "Major name",'autofocus': ''}),
      'address': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'placeholder': "Major address",'autofocus': ''}),
      'principal': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'placeholder': "Major principal",'autofocus': ''}),
      'campus': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'placeholder': "Major campus",'autofocus': ''})    
    }

class Major_modify(forms.ModelForm):
  class Meta:
    model = models.Major
    fields = ('name', 'address', 'principal','campus',)
    widgets = {
      'name': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'placeholder': "Major name",'autofocus': ''}),
      'address': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'placeholder': "Major address",'autofocus': ''}),
      'principal': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'placeholder': "Major principal",'autofocus': ''}),
      'campus': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'placeholder': "Major campus",'autofocus': ''}) 
    }
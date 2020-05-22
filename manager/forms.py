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

class myClass(forms.ModelForm): 
  class Meta:
    model = models.myClass
    fields = ('id', 'name', 'date', 'head_teacher', 'grade', 'major' )
    widgets = {
      'id': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'placeholder': "Class id",'autofocus': ''}),
      'name': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'placeholder': "Class name",'autofocus': ''}),
      'date': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'placeholder': "Set up date",'autofocus': ''}),
      'head_teacher':forms.TextInput(attrs={'class': 'form-control col-sm-10', 'placeholder': "Head teacher",'autofocus': ''}),
      'grade':forms.TextInput(attrs={'class': 'form-control col-sm-10', 'placeholder': "Grade",'autofocus': ''}),
      'major':forms.TextInput(attrs={'class': 'form-control col-sm-10', 'placeholder': "Major",'autofocus': ''}),
    }

class myClass_modify(forms.ModelForm):
  class Meta:
    model = models.myClass
    fields = ('name', 'date', 'head_teacher', 'grade', 'major' )
    widgets = {
      'name': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'placeholder': "Class name",'autofocus': ''}),
      'date': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'placeholder': "Set up date",'autofocus': ''}),
      'head_teacher':forms.TextInput(attrs={'class': 'form-control col-sm-10', 'placeholder': "Head teacher",'autofocus': ''}),
      'grade':forms.TextInput(attrs={'class': 'form-control col-sm-10', 'placeholder': "Grade",'autofocus': ''}),
      #'major':forms.TextInput(attrs={'class': 'form-control col-sm-10', 'placeholder': "Major",'autofocus': ''}),
    }
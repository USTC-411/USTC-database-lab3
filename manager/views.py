# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def IndexForStudent(request):
  return render(request, 'manager/IndexForStudent.html')

def login(request):
  return render(request, 'manager/login.html')



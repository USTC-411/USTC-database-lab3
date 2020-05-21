# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Person, Student, Lesson

# Create your views here.
def index(request):
  return render(request, 'manager/search.html')

def global_search(request):
  stu_list=[]
  stu={}
  global_info=""
  if request.method == "GET":
    global_info = request.GET.get('global_info').strip()
  if global_info:
    stu_list = Student.objects.filter(student_id__contains(global_info))

  return render(request,'manager/search.html',{'stu_list':stu_list})

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.db.models import Q
from .models import *

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
    stu_list = Student.objects.filter(Q(name__contains=StudentName) | Q(student_id__contains=StudentID)| Q(myClass__name__contains=global_info))
  return render(request,'manager/search.html',{'stu_list':stu_list})

def stu_search(request):
  stu_list = []
  stu={}
  if request.method == "GET":
    StudentID = request.GET.get('StudentID').strip()
    StudentName = request.GET.get('StudentName').strip()
    StudentClass = request.GET.get('StudentClass').strip()
    StudentSex = request.GET.get('StudentSex').strip()
  if StudentID or StudentName or StudentClass or StudentSex:
    stu_list = Student.objects.filter(Q(name__contains=StudentName) & Q(student_id__contains=StudentID) & Q(myClass__name__contains=StudentClass) & Q(sex__contains=StudentSex))
  return render(request,'manager/search.html',{'stu_list':stu_list})

def cou_search(request):
  cou_list=[]
  cou={}
  return render(request,'manager/search.html',{'cou_list':cou_list})

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
  cou_list=[]
  global_info=""
  if request.method == "GET":
    global_info = request.GET.get('global_info').strip()
  if global_info:
    stu_list = Student.objects.filter(Q(name__contains=global_info) | Q(student_id__contains=global_info)| Q(myClass__name__contains=global_info) | Q(nationality__contains=global_info))
    cou_list = ValidLesson.objects.filter(Q(lesson__name__contains=global_info) | Q(teacher__name__contains=global_info) | Q(lesson__id__contains=global_info) | Q(begin_time__contains=global_info) | Q(begin_semester__contains=global_info))
  return render(request,'manager/search.html',{'stu_list':stu_list,'cou_list':cou_list})

def stu_search(request):
  stu_list = []
  if request.method == "GET":
    StudentID = request.GET.get('StudentID').strip()
    StudentName = request.GET.get('StudentName').strip()
    StudentClass = request.GET.get('StudentClass').strip()
    StudentSex = request.GET.get('StudentSex').strip()
    StudentNation = request.GET.get('StudentNation').strip()
  if StudentID or StudentName or StudentClass or StudentSex or StudentNation:
    stu_list = Student.objects.filter(Q(name__contains=StudentName) & Q(student_id__contains=StudentID) & Q(myClass__name__contains=StudentClass) & Q(sex__contains=StudentSex) & Q(nationality__contains=StudentNation))
  return render(request,'manager/search.html',{'stu_list':stu_list})

def cou_search(request):
  cou_list=[]
  if request.method == "GET":
    CourseID = request.GET.get('CourseID').strip()
    CourseName = request.GET.get('CourseName').strip()
    CourseTeacher = request.GET.get('CourseTeacher').strip()
    CourseTime = request.GET.get('CourseTime').strip()
    CourseSemester = request.GET.get('CourseSemester').strip()
  if CourseID or CourseName or CourseTeacher or CourseTime or CourseSemester:
    cou_list = ValidLesson.objects.filter(Q(lesson__id__contains=CourseID) & Q(lesson__name__contains=CourseName) & Q(teacher__name__contains=CourseTeacher) & Q(begin_time__contains=CourseTime) & Q(begin_semester__contains=CourseSemester))
  return render(request,'manager/search.html',{'cou_list':cou_list})

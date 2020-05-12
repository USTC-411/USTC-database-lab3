# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Campus(models.Model):
  id = models.CharField(max_length=30, primary_key=True)
  name = models.CharField(max_length=30)
  address = models.CharField(max_length=30)
  def __str__(self):
      return self.name
  

class Major(models.Model):
  id = models.CharField(max_length=30, primary_key=True)
  name = models.CharField(max_length=30)
  address = models.CharField(max_length=30)
  principal = models.CharField(max_length=30)
  campus = models.ForeignKey('Campus', on_delete=models.CASCADE)
  def __str__(self):
    return self.name

class Class_(models.Model):
  id = models.CharField(max_length=30, primary_key=True)
  name = models.CharField(max_length=30)
  date = models.DateField()
  head_teacher = models.CharField(max_length=30)
  grade = models.DateField()
  major = models.ForeignKey('Major', on_delete=models.CASCADE)
  def __str__(self):
    return self.name

class Person(models.Model):
  # Enum value for id_type
  IDCARD = 'IDCard'
  PASSPORT = 'Passport'
  IDTYPE = (
    (IDCARD, '身份证')
    (PASSPORT, '护照')
  )
  # Enum value for sex
  MALE = 'male'
  FEMALE = 'female'
  SEXTYPE = (
    (MALE, '男')
    (FEMALE, '女')
  )
  # Fields for model
  id = models.CharField(max_length=30, primary_key=True)
  id_type = models.CharField(choices=IDTYPE, default=IDCARD)
  name = models.CharField(max_length=30)
  sex = models.CharField(choices=SEXTYPE)
  birthday = models.CharField(max_length=30)
  nationality = models.CharField(max_length=30)
  family_address = models.CharField(max_length=30, blank=True)
  family_postcode = models.CharField(max_length=30, blank=True)
  family_telephone = models.CharField(max_length=30, blank=True)
  entry_date = models.DateField()
  email = models.CharField(max_length=30)
  class Meta:
    abstract = True

class Teacher(Person):
  # Enum value for job title
  PROFESSOR = 'professor'
  ASSOCIATE_PROFESSOR = 'associate_professor'
  TITLETYPE = (
    (PROFESSOR, '教授')
    (ASSOCIATE_PROFESSOR, '副教授')
  )
  # Fields for model
  teacher_id = models.CharField(max_length=30, unique=True)
  major = models.ForeignKey('Major', on_delete=models.CASCADE)
  title = models.CharField(choices=TITLETYPE)
  def __str__(self):
    return self.name

class Student(Person):
  student_id = models.CharField(max_length=30, unique=True)
  class_ = models.ForeignKey('Class_', on_delete=models.CASCADE)
  def __str__(self):
    return self.name

class StatusChange(models.Model):
  chenge_id = models.CharField(max_length=30, primary_key=True)
  change_date = models.DateField()
  original_class = models.OneToOneField(Class_,on_delete=models.CASCADE)
  current_class = models.OneToOneField(Class_,on_delete=models.CASCADE)
  class Meta:
    abstract = True

class MajorTransfer(StatusChange):
  student = models.OneToOneField(
    Student,
    on_delete = models.CASCADE,
    related_name = 'major_transfer'
  )
  has_transfered_communist_youth_league_relationship = models.BooleanField(default=False)

class GradeTransfer(StatusChange):
  # Enum value of degrade reason
  SUSPENSION = 'suspension'
  VOLUNTEER_TEACHING = 'volunteer_teaching'
  DEGRADE_REASON = (
    (SUSPENSION, '休学')
    (VOLUNTEER_TEACHING, '支教')
  )
  # Fields of this model
  student = models.OneToOneField(
    Student,
    on_delete = models.CASCADE,
    related_name = 'grade_transfer'
  )
  degrade_reason = models.CharField(choices=DEGRADE_REASON)




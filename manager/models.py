# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
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

class myClass(models.Model):
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
  ID_TYPE = (
    (IDCARD, '身份证'),
    (PASSPORT, '护照')
  )
  # Enum value for sex
  MALE = 'male'
  FEMALE = 'female'
  SEX_TYPE = (
    (MALE, '男'),
    (FEMALE, '女')
  )
  # Fields for model
  id = models.CharField(max_length=30, primary_key=True)
  id_type = models.CharField(max_length=30,choices=ID_TYPE, default=IDCARD)
  name = models.CharField(max_length=30)
  sex = models.CharField(max_length=30, choices=SEX_TYPE)
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
  TITLE_TYPE = (
    (PROFESSOR, '教授'),
    (ASSOCIATE_PROFESSOR, '副教授')
  )
  # Fields for model
  teacher_id = models.CharField(max_length=30, unique=True)
  major = models.ForeignKey('Major', on_delete=models.CASCADE)
  title = models.CharField(max_length=30, choices=TITLE_TYPE)
  def __str__(self):
    return self.name

class Student(Person):
  student_id = models.CharField(max_length=30, unique=True)
  myClass = models.ForeignKey('myClass', on_delete=models.CASCADE)
  def __str__(self):
    return self.name

class StatusChange(models.Model):
  chenge_id = models.CharField(max_length=30, primary_key=True)
  change_date = models.DateField()
  class Meta:
    abstract = True

class MajorTransfer(StatusChange):
  student = models.OneToOneField(
    Student,
    on_delete = models.CASCADE,
    related_name = 'major_transfer'
  )
  original_class = models.OneToOneField(myClass, on_delete=models.CASCADE, related_name="major_original_class")
  current_class = models.OneToOneField(myClass, on_delete=models.CASCADE, related_name="major_current_class")
  has_transfered_communist_youth_league_relationship = models.BooleanField(default=False)

class GradeTransfer(StatusChange):
  # Enum value of degrade reason
  SUSPENSION = 'suspension'
  VOLUNTEER_TEACHING = 'volunteer_teaching'
  DEGRADE_REASON = (
    (SUSPENSION, '休学'),
    (VOLUNTEER_TEACHING, '支教')
  )
  # Fields of this model
  student = models.OneToOneField(
    Student,
    on_delete = models.CASCADE,
    related_name = 'grade_transfer'
  )
  original_class = models.OneToOneField(myClass, on_delete=models.CASCADE, related_name="degrade_original_class")
  current_class = models.OneToOneField(myClass, on_delete=models.CASCADE, related_name="degrade_current_class")
  degrade_reason = models.CharField(max_length=30, choices=DEGRADE_REASON)

class Lesson(models.Model):
  # Enum value of test type
  TEST = 'test'
  DEBATE = 'debate'
  TEST_TYPE = (
    (TEST, '考试'),
    (DEBATE, '答辩')
  )
  # Enum value of lesson status
  VALID = 'valid'
  INVALID = 'invalid'
  LESSON_STATUS = (
    (VALID, '开课'),
    (INVALID, '未开课')
  )
  # Fields of this model
  id = models.CharField(max_length=30, primary_key=True)
  name = models.CharField(max_length=30, unique=True)
  major = models.ForeignKey('Major', on_delete=models.CASCADE)
  test_type = models.CharField(max_length=30, choices=TEST_TYPE, default=TEST)
  lesson_status = models.CharField(max_length=30, choices=LESSON_STATUS, default=INVALID)

class ValidLesson(models.Model):
  # Enum value of semester
  SPRING = 'spring'
  AUTUMN = 'autumn'
  SEMESTER = (
    (SPRING, '春季学期'),
    (AUTUMN, '秋季学期')
  )
  # Enum value of lesson's begin time
  class BEGIN_TIME_TYPE(models.IntegerChoices):
    MONDAY1 = 11
    MONDAY2 = 12
    MONDAY3 = 13
    MONDAY4 = 14
    MONDAY5 = 15
    MONDAY6 = 16
    MONDAY7 = 17
    MONDAY8 = 18
    MONDAY9 = 19
    TUESDAY1 = 21
    TUESDAY2 = 22
    TUESDAY3 = 23
    TUESDAY4 = 24
    TUESDAY5 = 25
    TUESDAY6 = 26
    TUESDAY7 = 27
    TUESDAY8 = 28
    TUESDAY9 = 29
    WEDNESDAY1 = 31
    WEDNESDAY2 = 32
    WEDNESDAY3 = 33
    WEDNESDAY4 = 34
    WEDNESDAY5 = 35
    WEDNESDAY6 = 36
    WEDNESDAY7 = 37
    WEDNESDAY8 = 38
    WEDNESDAY9 = 39
    THURSDAY1 = 41
    THURSDAY2 = 42
    THURSDAY3 = 43
    THURSDAY4 = 44
    THURSDAY5 = 45
    THURSDAY6 = 46
    THURSDAY7 = 47
    THURSDAY8 = 48
    THURSDAY9 = 49
    FRIDAY1 = 51
    FRIDAY2 = 52
    FRIDAY3 = 53
    FRIDAY4 = 54
    FRIDAY5 = 55
    FRIDAY6 = 56
    FRIDAY7 = 57
    FRIDAY8 = 58
    FRIDAY9 = 59
  # Fields of this model
  lesson = models.OneToOneField(
    Lesson,
    on_delete=models.CASCADE,
    related_name='valid_status',
    null=True,
    blank=True
  )
  teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
  begin_date = models.DateField()
  begin_semester = models.CharField(max_length=30, choices=SEMESTER)
  begin_time = models.IntegerField(choices=BEGIN_TIME_TYPE.choices)
  students = models.ManyToManyField(Student, related_name='students', through='LessonSelect')

class LessonSelect(models.Model):
  valid_lesson = models.ForeignKey(ValidLesson, on_delete=models.CASCADE)
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  score = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)])


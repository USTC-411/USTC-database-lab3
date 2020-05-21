# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Campus(models.Model): # 校区模型的定义
  id = models.CharField(max_length=30, primary_key=True)
  name = models.CharField(max_length=30)
  address = models.CharField(max_length=30)
  def __str__(self):
      return self.name
  

class Major(models.Model): # 专业模型的定义
  id = models.CharField(max_length=30, primary_key=True)
  name = models.CharField(max_length=30)
  address = models.CharField(max_length=30)
  principal = models.CharField(max_length=30)
  campus = models.ForeignKey('Campus', on_delete=models.CASCADE) # 有一个外键，默认指向校区的主键，也就是id
  def __str__(self):
    return self.name

class myClass(models.Model): # 班级的模型定义，因为与关键字冲突，因此命名为myClass
  id = models.CharField(max_length=30, primary_key=True)
  name = models.CharField(max_length=30)
  date = models.DateField()
  head_teacher = models.CharField(max_length=30)
  grade = models.DateField()
  major = models.ForeignKey('Major', on_delete=models.CASCADE) # 有一个外键，默认指向专业的主键，也就是id
  def __str__(self):
    return self.name

class Person(models.Model): # 定义一个抽象类“人类”作为父类，子类为之后的教师和学生类
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
  
  class Meta: # Meta属性，定义模型的一些特性，此处约定该模型为抽象类
    abstract = True

class Teacher(Person): # 老师模型的定义，继承Person类
  # Enum value for job title
  PROFESSOR = 'professor'
  ASSOCIATE_PROFESSOR = 'associate_professor'
  TITLE_TYPE = (
    (PROFESSOR, '教授'),
    (ASSOCIATE_PROFESSOR, '副教授')
  )
  # Fields for model
  teacher_id = models.CharField(max_length=30, unique=True)
  password = models.CharField(max_length=256, default="123456")
  major = models.ForeignKey('Major', on_delete=models.CASCADE) # 有一个外键，默认指向专业的主键，也就是id
  title = models.CharField(max_length=30, choices=TITLE_TYPE)
  def __str__(self):
    return self.name

class Student(Person): # 学生模型的定义，继承Person类
  student_id = models.CharField(max_length=30, unique=True)
  password = models.CharField(max_length=256, default="123456")
  myClass = models.ForeignKey('myClass', on_delete=models.CASCADE) # 有一个外键，默认指向班级的主键，也就是id
  def __str__(self):
    return self.name

class StatusChange(models.Model): # 学籍异动的模型定义，作为一个抽象类，子类为之后定义的转专业和降级
  chenge_id = models.CharField(max_length=30, primary_key=True)
  change_date = models.DateField()
  class Meta:
    abstract = True

class MajorTransfer(StatusChange): # 转专业的模型定义，继承自学籍异动类
  student = models.OneToOneField( # 有一个一对一关系，一个学生只能有一条转专业记录，一条记录也只对应一个学生
    Student,
    on_delete = models.CASCADE,
    related_name = 'major_transfer'
  )
  # 有一个外键，默认指向班级的主键，可以在班级中通过major_original_class属性来访问这一条转专业记录
  original_class = models.ForeignKey('myClass', on_delete=models.CASCADE, related_name="major_original_class")
  # 有一个外键，默认指向班级的主键，可以在班级中通过major_current_class属性来访问
  current_class = models.ForeignKey('myClass', on_delete=models.CASCADE, related_name="major_current_class") 
  has_transfered_communist_youth_league_relationship = models.BooleanField(default=False)

class GradeTransfer(StatusChange): # 降级的模型定义，继承自学籍异动类
  # Enum value of degrade reason
  SUSPENSION = 'suspension'
  VOLUNTEER_TEACHING = 'volunteer_teaching'
  DEGRADE_REASON = (
    (SUSPENSION, '休学'),
    (VOLUNTEER_TEACHING, '支教')
  )
  # Fields of this model
  student = models.OneToOneField( # 有一个一对一关系，一个学生只能有一条降级记录，一条记录也只对应一个学生
    Student,
    on_delete = models.CASCADE,
    related_name = 'grade_transfer'
  )
  # 有一个外键，默认指向班级的主键，可以在班级中通过grade_original_class属性来访问
  original_class = models.ForeignKey('myClass', on_delete=models.CASCADE, related_name="grade_original_class")
  # 有一个外键，默认指向班级的主键，可以在班级中通过grade_original_class属性来访问
  current_class = models.ForeignKey('myClass', on_delete=models.CASCADE, related_name="grade_current_class")
  degrade_reason = models.CharField(max_length=30, choices=DEGRADE_REASON)

class Lesson(models.Model): # 课程模型的定义
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
  major = models.ForeignKey('Major', on_delete=models.CASCADE) # 有一个外键，默认指向专业的主键，也就是id
  test_type = models.CharField(max_length=30, choices=TEST_TYPE, default=TEST)
  lesson_status = models.CharField(max_length=30, choices=LESSON_STATUS, default=INVALID)

class ValidLesson(models.Model): # 有效课程的模型定义，有效课程指正在开课的课程，某些课可能存在但是这学期不开之类
  # Enum value of semester
  SPRING = 'spring'
  AUTUMN = 'autumn'
  SEMESTER = (
    (SPRING, '春季学期'),
    (AUTUMN, '秋季学期')
  )
  # Enum value of lesson's begin time
  class BEGIN_TIME_TYPE(models.IntegerChoices): # 开课时间的枚举类定义，建议折叠
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
  lesson = models.OneToOneField( # 有效课程和所有的课程之间有一个一对一关系
    Lesson,
    on_delete=models.CASCADE,
    related_name='valid_status',
    null=True,
    blank=True
  )
  teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE) # 有一个外键，指向开课的老师
  begin_date = models.DateField()
  begin_semester = models.CharField(max_length=30, choices=SEMESTER)
  begin_time = models.IntegerField(choices=BEGIN_TIME_TYPE.choices)
  # 与学生之间有一个多对多关系，关系的中间表为LessonSelect
  students = models.ManyToManyField(Student, related_name='students', through='LessonSelect') 

class LessonSelect(models.Model):
  # 这是选课表，是学生和有效课程的多对多关系中的中间表，某些参数通过关系来访问
  valid_lesson = models.ForeignKey(ValidLesson, on_delete=models.CASCADE)
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  score = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)])


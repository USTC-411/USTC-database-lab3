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
class Teacher(forms.ModelForm): 
  class Meta:
    model = models.Teacher
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
    # Enum value for job title
    PROFESSOR = 'professor'
    ASSOCIATE_PROFESSOR = 'associate_professor'
    TITLE_TYPE = (
      (PROFESSOR, '教授'),
      (ASSOCIATE_PROFESSOR, '副教授')
    )
    fields = (
      'id',
      'id_type',
      'name',
      'sex',
      'birthday',
      'nationality',
      'family_address',
      'family_postcode',
      'family_telephone',
      'entry_date',
      'email',
      'teacher_id',
      'password',
      'major',
      'title',
    )
    widgets = {
      'id': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'id_type': forms.Select(choices=ID_TYPE, attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'name': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'sex': forms.Select(choices=SEX_TYPE, attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'birthday': forms.DateInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'nationality': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'family_address': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'family_postcode': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'family_telephone': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'entry_date': forms.DateInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'email': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'teacher_id': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'password': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'major': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'title': forms.Select(choices=TITLE_TYPE, attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
    }

class Teacher_modify(forms.ModelForm): 
  class Meta:
    model = models.Teacher
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
    # Enum value for job title
    PROFESSOR = 'professor'
    ASSOCIATE_PROFESSOR = 'associate_professor'
    TITLE_TYPE = (
      (PROFESSOR, '教授'),
      (ASSOCIATE_PROFESSOR, '副教授')
    )
    fields = (
      'id_type',
      'name',
      'sex',
      'birthday',
      'nationality',
      'family_address',
      'family_postcode',
      'family_telephone',
      'entry_date',
      'email',
      'password',
      'major',
      'title',
    )
    widgets = {
      'id_type': forms.Select(choices=ID_TYPE, attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'name': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'sex': forms.Select(choices=SEX_TYPE, attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'birthday': forms.DateInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'nationality': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'family_address': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'family_postcode': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'family_telephone': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'entry_date': forms.DateInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'email': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'password': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'major': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'title': forms.Select(choices=TITLE_TYPE, attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
    }

class MajorTransfer(forms.ModelForm): 
  class Meta:
    model = models.MajorTransfer
    fields = ('change_id', 'change_date', 'student', 'original_class', 'current_class', 'has_transfered_communist_youth_league_relationship')
    widgets = {
      'change_id': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'change_date': forms.DateInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'student': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'original_class': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'current_class': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'has_transfered_communist_youth_league_relationship': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
    }

class MajorTransfer_modify(forms.ModelForm):
  class Meta:
    model = models.MajorTransfer
    fields = ('change_date', 'original_class', 'current_class', 'has_transfered_communist_youth_league_relationship')
    widgets = {
      'change_date': forms.DateInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'original_class': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'current_class': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'has_transfered_communist_youth_league_relationship': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
    }

class GradeTransfer(forms.ModelForm): 
  class Meta:
    model = models.GradeTransfer
    # Enum value of degrade reason
    SUSPENSION = 'suspension'
    VOLUNTEER_TEACHING = 'volunteer_teaching'
    DEGRADE_REASON = (
      (SUSPENSION, '休学'),
      (VOLUNTEER_TEACHING, '支教')
    )
    fields = ('change_id', 'change_date', 'student', 'original_class', 'current_class', 'degrade_reason')
    widgets = {
      'change_id': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'change_date': forms.DateInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'student': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'original_class': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'current_class': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'degrade_reason': forms.Select(choices=DEGRADE_REASON, attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
    }

class GradeTransfer_modify(forms.ModelForm):
  class Meta:
    model = models.GradeTransfer
    # Enum value of degrade reason
    SUSPENSION = 'suspension'
    VOLUNTEER_TEACHING = 'volunteer_teaching'
    DEGRADE_REASON = (
      (SUSPENSION, '休学'),
      (VOLUNTEER_TEACHING, '支教')
    )
    fields = ('change_date', 'original_class', 'current_class', 'degrade_reason')
    widgets = {
      'change_date': forms.DateInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'original_class': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'current_class': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'degrade_reason': forms.Select(choices=DEGRADE_REASON, attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
    }
class Lesson(forms.ModelForm):
  class Meta:
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
    model = models.Lesson
    fields = ('id','name', 'major', 'test_type','lesson_status',)
    widgets = {
      'id': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'placeholder': "Lesson id",'autofocus': ''}),
      'name': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'placeholder': "Lesson name",'autofocus': ''}),
      'major': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'placeholder': "Lesson major",'autofocus': ''}),
      'test_type': forms.Select(choices=TEST_TYPE,attrs={'class': 'form-control col-sm-10', 'placeholder': "Lesson test_type",'autofocus': ''}),
      'lesson_status': forms.Select(choices=LESSON_STATUS,attrs={'class': 'form-control col-sm-10', 'placeholder': "Lesson status",'autofocus': ''}),
    }


class Lesson_modify(forms.ModelForm):
  class Meta:
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
    model = models.Lesson
    fields = ('name', 'major', 'test_type','lesson_status',)
    widgets = {
      'name': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'placeholder': "Lesson name",'autofocus': ''}),
      'major': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'placeholder': "Lesson major",'autofocus': ''}),
      'test_type': forms.Select(choices=TEST_TYPE,attrs={'class': 'form-control col-sm-10', 'placeholder': "Lesson test_type",'autofocus': ''}),
      'lesson_status': forms.Select(choices=LESSON_STATUS,attrs={'class': 'form-control col-sm-10', 'placeholder': "Lesson status",'autofocus': ''}),
    }

class Student(forms.ModelForm):
  class Meta:
    model = models.Student
    # Enum value for id_type
    IDCARD = 'IDCard'
    PASSPORT = 'Passport'
    ID_TYPE = (
      (IDCARD, '身份证'),
      (PASSPORT, '护照'),
    )
    # Enum value for sex
    MALE = 'male'
    FEMALE = 'female'
    SEX_TYPE = (
      (MALE, '男'),
      (FEMALE, '女')
    )
    fields = (
      'id',
      'id_type',
      'name',
      'sex',
      'birthday',
      'nationality',
      'family_address',
      'family_postcode',
      'family_telephone',
      'entry_date',
      'email',
      'student_id',
      'password',
      'myClass',
    )
    widgets = {
      'id': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'id_type': forms.Select(choices=ID_TYPE, attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'name': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'sex': forms.Select(choices=SEX_TYPE, attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'birthday': forms.DateInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'nationality': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'family_address': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'family_postcode': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'family_telephone': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'entry_date': forms.DateInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'email': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'student_id': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'password': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'myClass': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
    }

class Student_modify(forms.ModelForm):
  
  class Meta:
    model = models.Student
    # Enum value for id_type
    IDCARD = 'IDCard'
    PASSPORT = 'Passport'
    ID_TYPE = (
      (IDCARD, '身份证'),
      (PASSPORT, '护照'),
    )
    # Enum value for sex
    MALE = 'male'
    FEMALE = 'female'
    SEX_TYPE = (
      (MALE, '男'),
      (FEMALE, '女')
    )
    fields = (
      'id_type',
      'name',
      'sex',
      'birthday',
      'nationality',
      'family_address',
      'family_postcode',
      'family_telephone',
      'entry_date',
      'email',
      'password',
      'myClass',
    )
    widgets = {
      'id_type': forms.Select(choices=ID_TYPE, attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'name': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'sex': forms.Select(choices=SEX_TYPE, attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'birthday': forms.DateInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'nationality': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'family_address': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'family_postcode': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'family_telephone': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'entry_date': forms.DateInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'email': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'password': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
      'myClass': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'autofocus': ''}),
    }

class LessonSelect(forms.ModelForm): 
  class Meta:
    model = models.LessonSelect
    fields = ('valid_lesson', 'student', 'score' )
    widgets = {
      'valid_lesson': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'placeholder': "Campus id",'autofocus': ''}),
      'student': forms.TextInput(attrs={'class': 'form-control col-sm-10', 'placeholder': "Campus name",'autofocus': ''}),
      'score': forms.IntegerField(attrs={'class': 'form-control col-sm-10', 'placeholder': "Campus address",'autofocus': ''})
    }

class LessonSelect_modify(forms.ModelForm):
  class Meta:
    model = models.LessonSelect
    fields = ('name', 'address', )
    widgets = {
      'score': forms.IntegerField(attrs={'class': 'form-control col-sm-10', 'placeholder': "Campus address",'autofocus': ''}),    
    }
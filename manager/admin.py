# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Campus)
admin.site.register(models.Major)
admin.site.register(models.myClass)
admin.site.register(models.Teacher)
admin.site.register(models.Student)
admin.site.register(models.GradeTransfer)
admin.site.register(models.MajorTransfer)
admin.site.register(models.ValidLesson)
admin.site.register(models.LessonSelect)
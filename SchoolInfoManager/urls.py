"""SchoolInfoManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from manager.DataManage import campus,major,teacher,major_transfer,lesson,grade_transfer,student,course,classes,lesson_select
from manager import views,search

urlpatterns = [
    path('', views.entrance),
    path('admin/', admin.site.urls),
    path('IndexForStudent/', views.IndexForStudent),
    path('search/',search.index),
    path('search/global_search/',search.global_search),
    path('search/stu_search/',search.stu_search),
    path('search/cou_search/',search.cou_search),
    path('IndexForTeacher/', views.IndexForTeacher),
    #path('login/', views.login),
    path('login_student/', views.login_student),
    path('logout_student/', views.logout_student),
    path('login_teacher/', views.login_teacher),
    path('logout_teacher/', views.logout_teacher),

    path('ManageCampus/', campus.campus),
    path('ManageCampus/add/', campus.add),
    path('ManageCampus/delete/', campus.delete),
    path('ManageCampus/query/', campus.query),
    path('ManageCampus/modify/', campus.modify),

    path('ManageClass/', classes.classes),
    path('ManageClass/add/', classes.add),
    path('ManageClass/delete/', classes.delete),
    path('ManageClass/query/', classes.query),
    path('ManageClass/modify/', classes.modify),

    path('ManageMajor/', major.major),
    path('ManageMajor/add/', major.add),
    path('ManageMajor/delete/', major.delete),
    path('ManageMajor/query/', major.query),
    path('ManageMajor/modify/', major.modify),

    path('ManageTeacher/', teacher.teacher),
    path('ManageTeacher/add/', teacher.add),
    path('ManageTeacher/delete/', teacher.delete),
    path('ManageTeacher/query/', teacher.query),
    path('ManageTeacher/modify/', teacher.modify),
    path('ManageMajorTransfer/', major_transfer.major_transfer),
    path('ManageMajorTransfer/add/', major_transfer.add),
    path('ManageMajorTransfer/delete/', major_transfer.delete),
    path('ManageMajorTransfer/query/', major_transfer.query),
    path('ManageMajorTransfer/modify/', major_transfer.modify),
    path('ManageLesson/', lesson.lesson),
    path('ManageLesson/add/', lesson.add),
    path('ManageLesson/delete/', lesson.delete),
    path('ManageLesson/query/', lesson.query),
    path('ManageLesson/modify/', lesson.modify),
    path('ManageGradeTransfer/', grade_transfer.grade_transfer),
    path('ManageGradeTransfer/add/', grade_transfer.add),
    path('ManageGradeTransfer/delete/', grade_transfer.delete),
    path('ManageGradeTransfer/query/', grade_transfer.query),
    path('ManageGradeTransfer/modify/', grade_transfer.modify),
    path('ManageStudent/', student.student),
    path('ManageStudent/add/', student.add),
    path('ManageStudent/delete/', student.delete),
    path('ManageStudent/query/', student.query),
    path('ManageStudent/modify/', student.modify),
    path('ManageLessonSelect/', lesson_select.lesson_select),
    path('ManageLessonSelect/add/', lesson_select.add),
    path('ManageLessonSelect/delete/', lesson_select.delete),
    path('ManageLessonSelect/query/', lesson_select.query),
    path('ManageLessonSelect/modify/', lesson_select.modify),
    path('ManageCourse/', course.course),
    path('ManageCourse/add/', course.add),
    path('ManageCourse/delete/', course.delete),
    path('ManageCourse/query/', course.query),
    path('ManageCourse/modify/', course.modify),
]


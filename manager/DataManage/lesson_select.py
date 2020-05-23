from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.db.models import Q
from .. import forms
from .. import models
from manager.DataManage.authority import getAuthority

def lesson_select(request):
    modify_tag = -1
    message = ''
    show_result = []
    validlesson_set = models.ValidLesson.objects.all()
    user_id = request.session['user_id']
    if request.GET.get('modify_tag'):
        modify_tag = request.GET.get('modify_tag')
    lesson_select_table = models.LessonSelect.objects.filter(student=user_id)
    for i in lesson_select_table:
        if i.score == None:
            valid_lesson = models.ValidLesson.objects.get(lesson=i.valid_lesson.id)
            show_result.append([0, valid_lesson.lesson.id, valid_lesson.begin_date, valid_lesson.begin_semester, 'NULL', 0])
        else:
            valid_lesson = models.ValidLesson.objects.get(lesson=i.valid_lesson.id)
            show_result.append([0, valid_lesson.lesson.id, valid_lesson.begin_date, valid_lesson.begin_semester, i.score, 0])
    lesson_select_form = forms.LessonSelect()
    lesson_select_modify_form = forms.LessonSelect_modify()
    return render(
        request,
        'manager/ManagePage/ManageLessonSelect.html',
        {
            'validlesson_set' : show_result,
            'lesson_select_form' : lesson_select_form,
            'modify_tag' : modify_tag,
            'lesson_select_modify_form' : lesson_select_modify_form,
            'message': message,
        }
    )

def add(request):
    message = ''
    if request.method == 'POST':
        add_form = forms.LessonSelect(request.POST)
        user_id = request.session['user_id']
        # 权限控制——这一部分用于判断账号类型，因为validlesson只有管理员能操作，所以以下直接不允许相关操作
        if add_form.is_valid():
            validlesson = add_form.cleaned_data.get('valid_lesson')
            validlesson_begin_score = add_form.cleaned_data.get('score')
            try: # 如果用户是学生
                request.session.get('user_type', 'Student')
                authority = True
                if authority:
                    this_student = models.Student.objects.get(student_id=user_id)
                    new_lesson_select = models.LessonSelect(valid_lesson=validlesson, student=this_student, score=validlesson_begin_score)
                    new_lesson_select.save()
                else:
                    message = 'Do not have the right of this operation'
            except:
                message = 'Please login'
        else:
            print(add_form.errors)
            message = "Please check what you've entered"
    # 渲染动态页面
    show_result = []
    validlesson_set = models.ValidLesson.objects.all()
    user_id = request.session['user_id']
    lesson_select_table = models.LessonSelect.objects.filter(student=user_id)
    for i in lesson_select_table:
        if i.score == None:
            valid_lesson = models.ValidLesson.objects.get(lesson=i.valid_lesson.id)
            show_result.append([0, valid_lesson.lesson.id, valid_lesson.begin_date, valid_lesson.begin_semester, 'NULL', 0])
        else:
            valid_lesson = models.ValidLesson.objects.get(lesson=i.valid_lesson.id)
            show_result.append([0, valid_lesson.lesson.id, valid_lesson.begin_date, valid_lesson.begin_semester, i.score, 0])
    lesson_select_form = forms.LessonSelect()
    lesson_select_modify_form = forms.LessonSelect_modify()
    return render(
        request,
        'manager/ManagePage/ManageLessonSelect.html',
        {
            'validlesson_set' : show_result,
            'lesson_select_form' : lesson_select_form,
            'modify_tag' : -1,
            'lesson_select_modify_form' : lesson_select_modify_form,
            'message': message,
        }
    )

def delete(request):
    to_be_deleted_id = request.GET.get('id')
    to_be_deleted = models.ValidLesson.objects.get(lesson=to_be_deleted_id)
    user_id = request.session['user_id']
    message = ""
    try: # 如果用户是teacher
        request.session.get('user_type', 'Teacher')
        authority = False
        if authority:
            models.LessonSelect.objects.get(valid_lesson=to_be_deleted_id, student=user_id).delete()
        else:
            message = 'Do not have the right of this operation'
    except:
        try: # 如果用户是student
            request.session.get('user_type', 'Student')
            authority = True
            if authority:
                models.LessonSelect.objects.get(valid_lesson=to_be_deleted_id, student=user_id).delete()
            else:
                message = 'Do not have the right of this operation'
        except:
            message = 'Please login'
    # 渲染动态页面
    show_result = []
    validlesson_set = models.ValidLesson.objects.all()
    user_id = request.session['user_id']
    lesson_select_table = models.LessonSelect.objects.filter(student=user_id)
    for i in lesson_select_table:
        if i.score == None:
            valid_lesson = models.ValidLesson.objects.get(lesson=i.valid_lesson.id)
            show_result.append([0, valid_lesson.lesson.id, valid_lesson.begin_date, valid_lesson.begin_semester, 'NULL', 0])
        else:
            valid_lesson = models.ValidLesson.objects.get(lesson=i.valid_lesson.id)
            show_result.append([0, valid_lesson.lesson.id, valid_lesson.begin_date, valid_lesson.begin_semester, i.score, 0])
    lesson_select_form = forms.LessonSelect()
    lesson_select_modify_form = forms.LessonSelect_modify()
    return render(
        request,
        'manager/ManagePage/ManageLessonSelect.html',
        {
            'validlesson_set' : show_result,
            'lesson_select_form' : lesson_select_form,
            'modify_tag' : -1,
            'lesson_select_modify_form' : lesson_select_modify_form,
            'message': message,
        }
    )

def query(request):
    show_result = [] # 这是最终展示给用户的搜索结果
    if  request.method == "GET":
        option = request.GET.get('option')
        query_val = request.GET.get('query_val')
        query_result = []
        user_id = request.session['user_id']
        lesson_select_table = models.LessonSelect.objects.filter(student=user_id)
        for i in lesson_select_table:
            if i.score == None:
                valid_lesson = models.ValidLesson.objects.get(lesson=i.valid_lesson.id)
                show_result.append([0, valid_lesson.lesson.id, valid_lesson.begin_date, valid_lesson.begin_semester, 'NULL', 0])
            else:
                valid_lesson = models.ValidLesson.objects.get(lesson=i.valid_lesson.id)
                show_result.append([0, valid_lesson.lesson.id, valid_lesson.begin_date, valid_lesson.begin_semester, i.score, 0])
        try: # 如果用户是student
            request.session.get('user_type', 'Student')
            if option == 'lesson_id': # 搜索所有结果，其中会有非法结果
                for i in show_result:
                    if i[1] == query_val:
                        query_result.append(i)
            elif option == 'begin_date':
                for i in show_result:
                    if i[2] == query_val:
                        query_result.append(i)
            elif option == 'begin_semester':
                for i in show_result:
                    if i[3] == query_val:
                        query_result.append(i)
            elif option == 'score':
                for i in show_result:
                    if str(i[4]) == query_val:
                        query_result.append(i)
        except:
            message = 'Please login'
        # 返回结果给页面
        lesson_select_form = forms.LessonSelect()
        lesson_select_modify_form = forms.LessonSelect_modify()
        return render(
            request,
            'manager/ManagePage/ManageLessonSelect.html',
            {
                'validlesson_set' : query_result,
                'lesson_select_form' : lesson_select_form,
                'modify_tag' : -1,
                'lesson_select_modify_form' : lesson_select_modify_form,
            }
        )

def modify(request):
    if request.method == 'POST':
        modify_form = forms.LessonSelect_modify(request.POST)
        message = ''
        user_id = request.session['user_id']
        print(modify_form.errors)
        if modify_form.is_valid():
            validlesson_score = modify_form.cleaned_data.get('score')
            tag = request.GET.get('tag')
            # try: # 如果用户是学生
            request.session.get('user_type', 'Student')
            authority = True
            if authority:
                to_be_modified = models.LessonSelect.objects.get(valid_lesson=tag, student=user_id)
                to_be_modified.score = validlesson_score
                to_be_modified.save()
            else:
                message = 'Do not have the right of this operation'
            # except:
            #     message = 'Please login'
            
        else:
            message = 'Please check out what you write'
    # 渲染动态页面
    show_result = []
    validlesson_set = models.ValidLesson.objects.all()
    user_id = request.session['user_id']
    lesson_select_table = models.LessonSelect.objects.filter(student=user_id)
    for i in lesson_select_table:
        if i.score == None:
            valid_lesson = models.ValidLesson.objects.get(lesson=i.valid_lesson.id)
            show_result.append([0, valid_lesson.lesson.id, valid_lesson.begin_date, valid_lesson.begin_semester, 'NULL', 0])
        else:
            valid_lesson = models.ValidLesson.objects.get(lesson=i.valid_lesson.id)
            show_result.append([0, valid_lesson.lesson.id, valid_lesson.begin_date, valid_lesson.begin_semester, i.score, 0])
    lesson_select_form = forms.LessonSelect()
    lesson_select_modify_form = forms.LessonSelect_modify()
    return render(
        request,
        'manager/ManagePage/ManageLessonSelect.html',
        {
            'validlesson_set' : show_result,
            'lesson_select_form' : lesson_select_form,
            'modify_tag' : -1,
            'lesson_select_modify_form' : lesson_select_modify_form,
            'message': message,
        }
    )

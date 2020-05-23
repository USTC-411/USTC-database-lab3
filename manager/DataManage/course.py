from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.db.models import Q
from .. import forms
from .. import models
from manager.DataManage.authority import getAuthority

def course(request):
    modify_tag = -1
    message = ''
    show_result = []
    validlesson_set = models.ValidLesson.objects.all()
    user_id = request.session['user_id']
    if request.GET.get('modify_tag'):
        modify_tag = request.GET.get('modify_tag')
    try: # 如果用户是老师
        request.session.get('user_type', 'Teacher')
        for result in validlesson_set: # 剔除所有结果中的非法结果
            authority = getAuthority('query', 'ValidLesson', 'Teacher', result.id, user_id) # 检查用户对该元素的query权限
            if authority:
                show_result.append(result)
    except:
        try: # 如果用户是学生
            request.session.get('user_type', 'Student')
            for result in validlesson_set: # 剔除所有结果中的非法结果
                authority = getAuthority('query', 'ValidLesson', 'Student', result.id, user_id) # 检查用户对该元素的query权限
                if authority:
                    show_result.append(result)
        except:
            message = 'Please login'
    validlesson_form = forms.ValidLesson()
    validlesson_modify_form = forms.ValidLesson_modify()
    return render(
        request,
        'manager/ManagePage/ManageCourse.html',
        {
            'validlesson_set' : show_result,
            'validlesson_form' : validlesson_form,
            'modify_tag' : modify_tag,
            'validlesson_modify_form' : validlesson_modify_form,
            'message': message,
        }
    )

def add(request):
    message = ''
    if request.method == 'POST':
        add_form = forms.ValidLesson(request.POST)
        user_id = request.session['user_id']
        # 权限控制——这一部分用于判断账号类型，因为validlesson只有管理员能操作，所以以下直接不允许相关操作
        if add_form.is_valid():
            validlesson_id = add_form.cleaned_data.get('lesson')
            validlesson_teacher = add_form.cleaned_data.get('teacher')
            validlesson_begin_date = add_form.cleaned_data.get('begin_date')
            validlesson_begin_semester = add_form.cleaned_data.get('begin_semester')
            validlesson_begin_time = add_form.cleaned_data.get('begin_time')
            try: # 如果用户是老师
                request.session.get('user_type', 'Teacher')
                authority = getAuthority('add', 'ValidLesson', 'Teacher', validlesson_id, user_id)
                if authority:
                    new_validlesson = models.ValidLesson(lesson=validlesson_id, teacher=validlesson_teacher,begin_date=validlesson_begin_date,begin_semester=validlesson_begin_semester, begin_time=validlesson_begin_time)
                    new_validlesson.save()
                else:
                    message = 'Do not have the right of this operation'
            except:
                try: # 如果用户是学生
                    request.session.get('user_type', 'Student')
                    authority = getAuthority('add', 'ValidLesson', 'Student', validlesson_id, user_id)
                    if authority:
                        new_validlesson = models.ValidLesson(lesson=validlesson_id, teacher=validlesson_teacher,begin_date=validlesson_begin_date,begin_semester=validlesson_begin_semester, begin_time=validlesson_begin_time)
                        new_validlesson.save()
                    else:
                        message = 'Do not have the right of this operation'
                except:
                    message = 'Please login'
        else:
            print(add_form.errors)
            message = "Please check what you've entered"
    # 渲染动态页面
    validlesson_set = models.ValidLesson.objects.all()
    show_result = []
    try: # 如果用户是老师
        request.session.get('user_type', 'Teacher')
        for result in validlesson_set: # 剔除所有结果中的非法结果
            authority = getAuthority('query', 'ValidLesson', 'Teacher', result.id, user_id) # 检查用户对该元素的query权限
            if authority:
                show_result.append(result)
    except:
        try: # 如果用户是学生
            request.session.get('user_type', 'Student')
            for result in validlesson_set: # 剔除所有结果中的非法结果
                authority = getAuthority('query', 'ValidLesson', 'Student', result.id, user_id) # 检查用户对该元素的query权限
                if authority:
                    show_result.append(result)
        except:
            message = 'Please login'
    validlesson_form = forms.ValidLesson()
    validlesson_modify_form = forms.ValidLesson_modify()
    return render(
        request,
        'manager/ManagePage/ManageCourse.html',
        {
            'validlesson_set' : show_result,
            'validlesson_form' : validlesson_form,
            'modify_tag' : -1,
            'validlesson_modify_form' : validlesson_modify_form,
            'message' : message
        }
    )

def delete(request):
    to_be_deleted_id = request.GET.get('id')
    to_be_deleted = models.ValidLesson.objects.get(lesson=to_be_deleted_id)
    user_id = request.session['user_id']
    message = ""
    try: # 如果用户是teacher
        request.session.get('user_type', 'Teacher')
        authority = getAuthority('delete', 'ValidLesson', 'Teacher', to_be_deleted_id, user_id)
        if authority:
                to_be_deleted.delete()
        else:
            message = 'Do not have the right of this operation'
    except:
        try: # 如果用户是student
            request.session.get('user_type', 'Student')
            authority = getAuthority('delete', 'ValidLesson', 'Student', to_be_deleted_id, user_id)
            if authority:
                to_be_deleted.delete()
            else:
                message = 'Do not have the right of this operation'
        except:
            message = 'Please login'
    validlesson_form = forms.ValidLesson()
    validlesson_modify_form = forms.ValidLesson_modify()
    validlesson_set = models.ValidLesson.objects.all()
    show_result = []
    try: # 如果用户是老师
        request.session.get('user_type', 'Teacher')
        for result in validlesson_set: # 剔除所有结果中的非法结果
            authority = getAuthority('query', 'ValidLesson', 'Teacher', result.id, user_id) # 检查用户对该元素的query权限
            if authority:
                show_result.append(result)
    except:
        try: # 如果用户是学生
            request.session.get('user_type', 'Student')
            for result in validlesson_set: # 剔除所有结果中的非法结果
                authority = getAuthority('query', 'ValidLesson', 'Student', result.id, user_id) # 检查用户对该元素的query权限
                if authority:
                    show_result.append(result)
        except:
            message = 'Please login'
    return render(
        request,
        'manager/ManagePage/ManageCourse.html',
        {
            'validlesson_set' : show_result,
            'validlesson_form' : validlesson_form,
            'modify_tag' : -1,
            'message': message,
            'validlesson_modify_form' : validlesson_modify_form,
        }
    )

def query(request):
    show_result = [] # 这是最终展示给用户的搜索结果
    if  request.method == "GET":
        option = request.GET.get('option')
        query_val = request.GET.get('query_val')
        query_result = []
        user_id = request.session['user_id']
        try: # 如果用户是teacher
            request.session.get('user_type', 'Teacher')
            if option == 'lesson_id': # 搜索所有结果，其中会有非法结果
                query_result = models.ValidLesson.objects.filter(lesson=query_val)
            elif option == 'teacher_id':
                query_result = models.ValidLesson.objects.filter(teacher=query_val)
            elif option == 'begin_date':
                query_result = models.ValidLesson.objects.filter(begin_date=query_val)
            elif option == 'begin_semester':
                query_result = models.ValidLesson.objects.filter(begin_semester=query_val)
            elif option == 'begin_time':
                query_result = models.ValidLesson.objects.filter(begin_time=query_val)
            for result in query_result: # 剔除所有结果中的非法结果
                authority = getAuthority('query', 'ValidLesson', 'Teacher', result.id, user_id) # 检查用户对该元素的query权限
                if authority:
                    show_result.append(result)
        except:
            try: # 如果用户是student
                request.session.get('user_type', 'Student')
                if option == 'lesson_id': # 搜索所有结果，其中会有非法结果
                    query_result = models.ValidLesson.objects.filter(lesson=query_val)
                elif option == 'teacher_id':
                    query_result = models.ValidLesson.objects.filter(teacher=query_val)
                elif option == 'begin_date':
                    query_result = models.ValidLesson.objects.filter(begin_date=query_val)
                elif option == 'begin_semester':
                    query_result = models.ValidLesson.objects.filter(begin_semester=query_val)
                elif option == 'begin_time':
                    query_result = models.ValidLesson.objects.filter(begin_time=query_val)
                for result in query_result: # 剔除所有结果中的非法结果
                    authority = getAuthority('query', 'ValidLesson', 'Student', result.id, user_id) # 检查用户对该元素的query权限
                    if authority:
                        show_result.append(result)
            except:
                message = 'Please login'
        # 返回结果给页面
        validlesson_form = forms.ValidLesson()
        validlesson_modify_form = forms.ValidLesson_modify()
        return render(
            request,
            'manager/ManagePage/ManageCourse.html',
            {
                'validlesson_set' : show_result,
                'validlesson_form' : validlesson_form,
                'modify_tag' : -1,
                'validlesson_modify_form' : validlesson_modify_form,
            }
        )

def modify(request):
    if request.method == 'POST':
        modify_form = forms.ValidLesson_modify(request.POST)
        message = ''
        user_id = request.session['user_id']
        if modify_form.is_valid():
            validlesson_teacher = modify_form.cleaned_data.get('teacher')
            validlesson_begin_date = modify_form.cleaned_data.get('begin_date')
            validlesson_begin_semester = modify_form.cleaned_data.get('begin_semester')
            validlesson_begin_time = modify_form.cleaned_data.get('begin_time')
            tag = request.GET.get('tag')
            to_be_modified = models.ValidLesson.objects.get(lesson=tag)
            print(to_be_modified.lesson.id)
            try: # 如果用户是老师
                request.session.get('user_type', 'Teacher')
                authority = getAuthority('modify', 'ValidLesson', 'Teacher', tag, user_id)
                if authority:
                    to_be_modified.teacher = validlesson_teacher
                    to_be_modified.begin_date = validlesson_begin_date
                    to_be_modified.begin_semester = validlesson_begin_semester
                    to_be_modified.begin_time = validlesson_begin_time
                    to_be_modified.save()
                else:
                    message = 'Do not have the right of this operation'
            except: 
                try: # 如果用户是学生
                    request.session.get('user_type', 'Student')
                    authority = getAuthority('modify', 'ValidLesson', 'Student', tag, user_id)
                    if authority:
                        to_be_modified.teacher = validlesson_teacher
                        to_be_modified.begin_date = validlesson_begin_date
                        to_be_modified.begin_semester = validlesson_begin_semester
                        to_be_modified.begin_time = validlesson_begin_time
                        to_be_modified.save()
                    else:
                        message = 'Do not have the right of this operation'
                except:
                    message = 'Please login'
            
        else:
            message = 'Please check out what you write'
    # 渲染动态页面
    validlesson_set = models.ValidLesson.objects.all()
    show_result = []
    try: # 如果用户是老师
        request.session.get('user_type', 'Teacher')
        for result in validlesson_set: # 剔除所有结果中的非法结果
            authority = getAuthority('query', 'ValidLesson', 'Teacher', result.id, user_id) # 检查用户对该元素的query权限
            if authority:
                show_result.append(result)
    except:
        try: # 如果用户是学生
            request.session.get('user_type', 'Student')
            for result in validlesson_set: # 剔除所有结果中的非法结果
                authority = getAuthority('query', 'ValidLesson', 'Student', result.id, user_id) # 检查用户对该元素的query权限
                if authority:
                    show_result.append(result)
        except:
            message = 'Please login'
    validlesson_form = forms.ValidLesson()
    validlesson_modify_form = forms.ValidLesson_modify()
    return render(
        request,
        'manager/ManagePage/ManageCourse.html',
        {
            'validlesson_set' : validlesson_set,
            'validlesson_form' : validlesson_form,
            'modify_tag' : -1,
            'message' : message,
            'validlesson_modify_form' : validlesson_modify_form,
        }
    )

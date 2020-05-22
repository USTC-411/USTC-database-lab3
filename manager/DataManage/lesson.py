from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.db.models import Q
from .. import forms
from .. import models
from manager.DataManage.authority import getAuthority

def lesson(request):
    modify_tag = -1
    message = ''
    show_result = []
    lesson_set = models.Lesson.objects.all()
    user_id = request.session['user_id']
    if request.GET.get('modify_tag'):
        modify_tag = request.GET.get('modify_tag')
    try: # 如果用户是老师
        request.session.get('user_type', 'Teacher')
        for result in lesson_set: # 剔除所有结果中的非法结果
            authority = getAuthority('query', 'Lesson', 'Teacher', result.id, user_id) # 检查用户对该元素的query权限
            if authority:
                show_result.append(result)
    except:
        try: # 如果用户是学生
            request.session.get('user_type', 'Student')
            for result in lesson_set: # 剔除所有结果中的非法结果
                authority = getAuthority('query', 'Lesson', 'Student', result.id, user_id) # 检查用户对该元素的query权限
                if authority:
                    show_result.append(result)
        except:
            message = 'Please login'
    lesson_form = forms.Lesson()
    lesson_modify_form = forms.Lesson_modify()
    return render(
        request,
        'manager/ManagePage/ManageLesson.html',
        {
            'lesson_set' : show_result,
            'lesson_form' : lesson_form,
            'modify_tag' : modify_tag,
            'lesson_modify_form' : lesson_modify_form,
            'message': message,
        }
    )

def add(request):
    message = ''
    if request.method == 'POST':
        add_form = forms.Lesson(request.POST)
        user_id = request.session['user_id']
        # 权限控制——这一部分用于判断账号类型，因为lesson只有管理员能操作，所以以下直接不允许相关操作
        if add_form.is_valid():
            lesson_id = add_form.cleaned_data.get('id')
            lesson_name = add_form.cleaned_data.get('name')
            lesson_major = add_form.cleaned_data.get('major')
            lesson_test_type = add_form.cleaned_data.get('test_type')
            lesson_status = add_form.cleaned_data.get('lesson_status')
            try: # 如果用户是老师
                request.session.get('user_type', 'Teacher')
                authority = getAuthority('add', 'Lesson', 'Teacher', lesson_id, user_id)
                if authority:
                    lesson_major_in = models.Major.objects.get(name = lesson_major)
                    new_lesson = models.Lesson(lesson_id, lesson_name,major=lesson_major_in,test_type=lesson_test_type, lesson_status=lesson_status)
                    new_lesson.save()
                else:
                    message = 'Do not have the right of this operation'
            except:
                try: # 如果用户是学生
                    request.session.get('user_type', 'Student')
                    authority = getAuthority('add', 'Lesson', 'Student', lesson_id, user_id)
                    if authority:
                        lesson_major_in = models.Major.objects.get(name = lesson_major)
                        new_lesson = models.Lesson(lesson_id, lesson_name,major=lesson_major_in,test_type=lesson_test_type, lesson_status=lesson_status)
                        new_lesson.save()
                    else:
                        message = 'Do not have the right of this operation'
                except:
                    message = 'Please login'
        else:
            message = "Please check what you've entered"
    # 渲染动态页面
    lesson_set = models.Lesson.objects.all()
    show_result = []
    try: # 如果用户是老师
        request.session.get('user_type', 'Teacher')
        for result in lesson_set: # 剔除所有结果中的非法结果
            authority = getAuthority('query', 'Lesson', 'Teacher', result.id, user_id) # 检查用户对该元素的query权限
            if authority:
                show_result.append(result)
    except:
        try: # 如果用户是学生
            request.session.get('user_type', 'Student')
            for result in lesson_set: # 剔除所有结果中的非法结果
                authority = getAuthority('query', 'Lesson', 'Student', result.id, user_id) # 检查用户对该元素的query权限
                if authority:
                    show_result.append(result)
        except:
            message = 'Please login'
    lesson_form = forms.Lesson()
    lesson_modify_form = forms.Lesson_modify()
    return render(
        request,
        'manager/ManagePage/ManageLesson.html',
        {
            'lesson_set' : show_result,
            'lesson_form' : lesson_form,
            'modify_tag' : -1,
            'lesson_modify_form' : lesson_modify_form,
            'message' : message
        }
    )

def delete(request):
    to_be_deleted_id = request.GET.get('id')
    to_be_deleted = models.Lesson.objects.get(id=to_be_deleted_id)
    user_id = request.session['user_id']
    message = ""
    try: # 如果用户是teacher
        request.session.get('user_type', 'Teacher')
        authority = getAuthority('delete', 'Lesson', 'Teacher', to_be_deleted_id, user_id)
        if authority:
            try:
                to_be_deleted.valid_status   
                message = "You cannot delete it, because it's referenced by others"
            except:
                to_be_deleted.delete()
        else:
            message = 'Do not have the right of this operation'
    except:
        try: # 如果用户是student
            request.session.get('user_type', 'Student')
            authority = getAuthority('delete', 'Lesson', 'Student', to_be_deleted_id, user_id)
            if authority:
                try:
                    to_be_deleted.valid_status   
                    message = "You cannot delete it, because it's referenced by others"
                except:
                    to_be_deleted.delete()
            else:
                message = 'Do not have the right of this operation'
        except:
            message = 'Please login'
    lesson_form = forms.Lesson()
    lesson_modify_form = forms.Lesson_modify()
    lesson_set = models.Lesson.objects.all()
    show_result = []
    try: # 如果用户是老师
        request.session.get('user_type', 'Teacher')
        for result in lesson_set: # 剔除所有结果中的非法结果
            authority = getAuthority('query', 'Lesson', 'Teacher', result.id, user_id) # 检查用户对该元素的query权限
            if authority:
                show_result.append(result)
    except:
        try: # 如果用户是学生
            request.session.get('user_type', 'Student')
            for result in lesson_set: # 剔除所有结果中的非法结果
                authority = getAuthority('query', 'Lesson', 'Student', result.id, user_id) # 检查用户对该元素的query权限
                if authority:
                    show_result.append(result)
        except:
            message = 'Please login'
    return render(
        request,
        'manager/ManagePage/ManageLesson.html',
        {
            'lesson_set' : show_result,
            'lesson_form' : lesson_form,
            'modify_tag' : -1,
            'message': message,
            'lesson_modify_form' : lesson_modify_form,
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
            if option == 'id': # 搜索所有结果，其中会有非法结果
                query_result = models.Lesson.objects.filter(id=query_val)
            elif option == 'name':
                query_result = models.Lesson.objects.filter(name=query_val)
            elif option == 'major':
                query_result = models.Lesson.objects.filter(major=query_val)
            elif option == 'test_type':
                query_result = models.Lesson.objects.filter(test_type=query_val)
            elif option == 'lesson_status':
                query_result = models.Lesson.objects.filter(lesson_status=query_val)
            for result in query_result: # 剔除所有结果中的非法结果
                authority = getAuthority('query', 'Lesson', 'Teacher', result.id, user_id) # 检查用户对该元素的query权限
                if authority:
                    show_result.append(result)
        except:
            try: # 如果用户是student
                request.session.get('user_type', 'Student')
                if option == 'id': # 搜索所有结果，其中会有非法结果
                    query_result = models.Lesson.objects.filter(id=query_val)
                elif option == 'name':
                    query_result = models.Lesson.objects.filter(name=query_val)
                elif option == 'major':
                    query_result = models.Lesson.objects.filter(major=query_val)
                elif option == 'test_type':
                    query_result = models.Lesson.objects.filter(test_type=query_val)
                elif option == 'lesson_status':
                    query_result = models.Lesson.objects.filter(lesson_status=query_val)
                for result in query_result: # 剔除所有结果中的非法结果
                    authority = getAuthority('query', 'Lesson', 'Student', result.id, user_id) # 检查用户对该元素的query权限
                    if authority:
                        show_result.append(result)
            except:
                message = 'Please login'
        # 返回结果给页面
        lesson_form = forms.Lesson()
        lesson_modify_form = forms.Lesson_modify()
        return render(
            request,
            'manager/ManagePage/ManageLesson.html',
            {
                'lesson_set' : show_result,
                'lesson_form' : lesson_form,
                'modify_tag' : -1,
                'lesson_modify_form' : lesson_modify_form,
            }
        )

def modify(request):
    if request.method == 'POST':
        modify_form = forms.Lesson_modify(request.POST)
        message = ''
        user_id = request.session['user_id']
        if modify_form.is_valid():
            lesson_name = modify_form.cleaned_data.get('name')
            lesson_address = modify_form.cleaned_data.get('address')
            lesson_major = modify_form.cleaned_data.get('major')
            lesson_test_type = modify_form.cleaned_data.get('test_type')
            lesson_status = modify_form.cleaned_data.get('lesson_status')
            tag = request.GET.get('tag')
            to_be_modified = models.Lesson.objects.get(id=tag)
            try: # 如果用户是老师
                request.session.get('user_type', 'Teacher')
                authority = getAuthority('modify', 'Lesson', 'Teacher', tag, user_id)
                if authority:
                    to_be_modified.name = lesson_name
                    to_be_modified.address = lesson_address
                    to_be_modified.major = lesson_major
                    to_be_modified.test_type = lesson_test_type
                    to_be_modified.lesson_status = lesson_status
                    to_be_modified.save()
                else:
                    message = 'Do not have the right of this operation'
            except: 
                try: # 如果用户是学生
                    request.session.get('user_type', 'Student')
                    authority = getAuthority('modify', 'Lesson', 'Student', tag, user_id)
                    if authority:
                        to_be_modified.name = lesson_name
                        to_be_modified.address = lesson_address
                        to_be_modified.major = lesson_major
                        to_be_modified.test_type = lesson_test_type
                        to_be_modified.lesson_status = lesson_status
                        to_be_modified.save()
                    else:
                        message = 'Do not have the right of this operation'
                except:
                    message = 'Please login'
            
        else:
            message = 'Please check out what you write'
    # 渲染动态页面
    lesson_set = models.Lesson.objects.all()
    show_result = []
    try: # 如果用户是老师
        request.session.get('user_type', 'Teacher')
        for result in lesson_set: # 剔除所有结果中的非法结果
            authority = getAuthority('query', 'Lesson', 'Teacher', result.id, user_id) # 检查用户对该元素的query权限
            if authority:
                show_result.append(result)
    except:
        try: # 如果用户是学生
            request.session.get('user_type', 'Student')
            for result in lesson_set: # 剔除所有结果中的非法结果
                authority = getAuthority('query', 'Lesson', 'Student', result.id, user_id) # 检查用户对该元素的query权限
                if authority:
                    show_result.append(result)
        except:
            message = 'Please login'
    lesson_form = forms.Lesson()
    lesson_modify_form = forms.Lesson_modify()
    return render(
        request,
        'manager/ManagePage/ManageLesson.html',
        {
            'lesson_set' : lesson_set,
            'lesson_form' : lesson_form,
            'modify_tag' : -1,
            'message' : message,
            'lesson_modify_form' : lesson_modify_form,
        }
    )

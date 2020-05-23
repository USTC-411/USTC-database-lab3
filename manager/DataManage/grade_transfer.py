# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.db.models import Q
from .. import forms
from .. import models
from manager.DataManage.authority import getAuthority

def grade_transfer(request):
    modify_tag = -1
    message = ''
    show_result = []
    grade_transfer_set = models.GradeTransfer.objects.all()
    user_id = request.session['user_id']
    if request.GET.get('modify_tag'):
        modify_tag = request.GET.get('modify_tag')
    try: # 如果用户是老师
        request.session.get('user_type', 'Teacher')
        for result in grade_transfer_set: # 剔除所有结果中的非法结果
            authority = getAuthority('query', 'GradeTransfer', 'Teacher', result.student.student_id, user_id) # 检查用户对该元素的query权限
            if authority:
                show_result.append(result)
    except:
        try: # 如果用户是学生
            request.session.get('user_type', 'Student')
            for result in grade_transfer_set: # 剔除所有结果中的非法结果
                authority = getAuthority('query', 'GradeTransfer', 'Student', result.student.student_id, user_id) # 检查用户对该元素的query权限
                if authority:
                    show_result.append(result)
        except:
            message = 'Please login'
    grade_transfer_form = forms.GradeTransfer()
    grade_transfer_modify_form = forms.GradeTransfer_modify()
    return render(
        request,
        'manager/ManagePage/ManageGradeTransfer.html',
        {
            'grade_transfer_set' : show_result,
            'grade_transfer_form' : grade_transfer_form,
            'modify_tag' : modify_tag,
            'grade_transfer_modify_form' : grade_transfer_modify_form,
            'message': message,
        }
    )

def add(request):
    message = ''
    if request.method == 'POST':
        add_form = forms.GradeTransfer(request.POST)
        user_id = request.session['user_id']
        print(add_form.errors)
        # 权限控制——这一部分用于判断账号类型，因为grade_transfer只有管理员能操作，所以以下直接不允许相关操作
        if add_form.is_valid():
            grade_transfer_change_id = add_form.cleaned_data.get('change_id')
            grade_transfer_change_date = add_form.cleaned_data.get('change_date')
            grade_transfer_student = add_form.cleaned_data.get('student')
            grade_transfer_original_class = add_form.cleaned_data.get('original_class')
            grade_transfer_current_class = add_form.cleaned_data.get('current_class')
            grade_transfer_degrade_reason = add_form.cleaned_data.get('degrade_reason')
            try: # 如果用户是老师
                request.session.get('user_type', 'Teacher')
                authority = getAuthority('add', 'GradeTransfer', 'Teacher', models.Student.objects.get(name=grade_transfer_student).student_id, user_id)
                if authority:
                    if grade_transfer_student.myClass == grade_transfer_original_class:
                        original = models.myClass.objects.get(name = grade_transfer_original_class)
                        current = models.myClass.objects.get(name = grade_transfer_current_class)
                        student = models.Student.objects.get(name = grade_transfer_student)
                        print(original, current)
                        new_grade_transfer = models.GradeTransfer(
                            change_id = grade_transfer_change_id,
                            change_date = grade_transfer_change_date,
                            student = grade_transfer_student,
                            original_class = original,
                            current_class = current,
                            degrade_reason = grade_transfer_degrade_reason,
                        )
                        new_grade_transfer.save()
                        print(grade_transfer_student.student_id)
                        target =  models.Student.objects.get(student_id = grade_transfer_student.student_id)
                        target.myClass = grade_transfer_current_class
                        target.save()
                    else:
                        message = 'Invalid operation'
                else:
                    message = 'Do not have the right of this operation'
            except:
                try: # 如果用户是学生
                    request.session.get('user_type', 'Student')
                    authority = getAuthority('add', 'GradeTransfer', 'Teacher', grade_transfer_student.student_id, user_id)
                    if authority:
                        new_grade_transfer = models.GradeTransfer(
                            grade_transfer_change_id,
                            grade_transfer_change_date,
                            grade_transfer_student,
                            grade_transfer_original_class,
                            grade_transfer_current_class,
                            grade_transfer_degrade_reason,
                        )
                        new_grade_transfer.save()
                    else:
                        message = 'Do not have the right of this operation'
                except:
                    message = 'Please login'
        else:
            message = "Please check what you've entered"
    # 渲染动态页面
    grade_transfer_set = models.GradeTransfer.objects.all()
    show_result = []
    try: # 如果用户是老师
        request.session.get('user_type', 'Teacher')
        for result in grade_transfer_set: # 剔除所有结果中的非法结果
            authority = getAuthority('query', 'GradeTransfer', 'Teacher', result.student.student_id, user_id) # 检查用户对该元素的query权限
            if authority:
                show_result.append(result)
    except:
        try: # 如果用户是学生
            request.session.get('user_type', 'Student')
            for result in grade_transfer_set: # 剔除所有结果中的非法结果
                authority = getAuthority('query', 'GradeTransfer', 'Student', result.student.student_id, user_id) # 检查用户对该元素的query权限
                if authority:
                    show_result.append(result)
        except:
            message = 'Please login'
    grade_transfer_form = forms.GradeTransfer()
    grade_transfer_modify_form = forms.GradeTransfer_modify()
    return render(
        request,
        'manager/ManagePage/ManageGradeTransfer.html',
        {
            'grade_transfer_set' : show_result,
            'grade_transfer_form' : grade_transfer_form,
            'modify_tag' : -1,
            'grade_transfer_modify_form' : grade_transfer_modify_form,
            'message' : message
        }
    )

def delete(request):
    to_be_deleted_id = request.GET.get('id')
    print(to_be_deleted_id)
    to_be_deleted = models.GradeTransfer.objects.get(change_id=to_be_deleted_id)
    user_id = request.session['user_id']
    message = ""
    try: # 如果用户是teacher
        request.session.get('user_type', 'Teacher')
        authority = getAuthority('delete', 'GradeTransfer', 'Teacher', to_be_deleted_id, user_id)
        if authority:
            to_be_deleted.delete()
        else:
            message = 'Do not have the right of this operation'
    except:
        try: # 如果用户是student
            request.session.get('user_type', 'Student')
            authority = getAuthority('delete', 'GradeTransfer', 'Student', to_be_deleted_id, user_id)
            if authority:
                to_be_deleted.delete()
            else:
                message = 'Do not have the right of this operation'
        except:
            message = 'Please login'
    grade_transfer_form = forms.GradeTransfer()
    grade_transfer_modify_form = forms.GradeTransfer_modify()
    grade_transfer_set = models.GradeTransfer.objects.all()
    show_result = []
    try: # 如果用户是老师
        request.session.get('user_type', 'Teacher')
        for result in grade_transfer_set: # 剔除所有结果中的非法结果
            authority = getAuthority('query', 'GradeTransfer', 'Teacher', result.student.student_id, user_id) # 检查用户对该元素的query权限
            if authority:
                show_result.append(result)
    except:
        try: # 如果用户是学生
            request.session.get('user_type', 'Student')
            for result in grade_transfer_set: # 剔除所有结果中的非法结果
                authority = getAuthority('query', 'GradeTransfer', 'Student', result.student.student_id, user_id) # 检查用户对该元素的query权限
                if authority:
                    show_result.append(result)
        except:
            message = 'Please login'
    return render(
        request,
        'manager/ManagePage/ManageGradeTransfer.html',
        {
            'grade_transfer_set' : show_result,
            'grade_transfer_form' : grade_transfer_form,
            'modify_tag' : -1,
            'message': message,
            'grade_transfer_modify_form' : grade_transfer_modify_form,
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
            if option == 'change_id': # 搜索所有结果，其中会有非法结果
                query_result = models.GradeTransfer.objects.filter(change_id=query_val)
            elif option == 'change_date':
                query_result = models.GradeTransfer.objects.filter(change_date=query_val)
            elif option == 'student':
                query_result = models.GradeTransfer.objects.filter(student=query_val)
            elif option == 'original_class':
                query_result = models.GradeTransfer.objects.filter(original_class=query_val)
            elif option == 'current_class':
                query_result = models.GradeTransfer.objects.filter(current_class=query_val)
            elif option == 'relationship':
                query_result = models.GradeTransfer.objects.filter(degrade_reason=query_val)
            for result in query_result: # 剔除所有结果中的非法结果
                authority = getAuthority('query', 'GradeTransfer', 'Teacher', result.student.student_id, user_id) # 检查用户对该元素的query权限
                if authority:
                    show_result.append(result)
        except:
            try: # 如果用户是student
                request.session.get('user_type', 'Student')
                if option == 'change_id': # 搜索所有结果，其中会有非法结果
                    query_result = models.GradeTransfer.objects.filter(change_id=query_val)
                elif option == 'change_date':
                    query_result = models.GradeTransfer.objects.filter(change_date=query_val)
                elif option == 'student':
                    query_result = models.GradeTransfer.objects.filter(student=query_val)
                elif option == 'original_class':
                    query_result = models.GradeTransfer.objects.filter(original_class=query_val)
                elif option == 'current_class':
                    query_result = models.GradeTransfer.objects.filter(current_class=query_val)
                elif option == 'relationship':
                    query_result = models.GradeTransfer.objects.filter(degrade_reason=query_val)
                for result in query_result: # 剔除所有结果中的非法结果
                    authority = getAuthority('query', 'GradeTransfer', 'Student', result.student.student_id, user_id) # 检查用户对该元素的query权限
                    if authority:
                        show_result.append(result)
            except:
                message = 'Please login'
        # 返回结果给页面
        grade_transfer_form = forms.GradeTransfer()
        grade_transfer_modify_form = forms.GradeTransfer_modify()
        return render(
            request,
            'manager/ManagePage/ManageGradeTransfer.html',
            {
                'grade_transfer_set' : show_result,
                'grade_transfer_form' : grade_transfer_form,
                'modify_tag' : -1,
                'grade_transfer_modify_form' : grade_transfer_modify_form,
            }
        )

def modify(request):
    if request.method == 'POST':
        modify_form = forms.GradeTransfer_modify(request.POST)
        message = ''
        user_id = request.session['user_id']
        print(modify_form.errors)
        if modify_form.is_valid():
            grade_transfer_change_date = modify_form.cleaned_data.get('change_date')
            grade_transfer_original_class = modify_form.cleaned_data.get('original_class')
            grade_transfer_current_class = modify_form.cleaned_data.get('current_class')
            grade_transfer_degrade_reason = modify_form.cleaned_data.get('degrade_reason')
            tag = request.GET.get('tag')
            to_be_modified = models.GradeTransfer.objects.get(change_id=tag)
            try: # 如果用户是老师
                request.session.get('user_type', 'Teacher')
                authority = getAuthority('modify', 'GradeTransfer', 'Teacher', tag, user_id)
                if authority:
                    to_be_modified.change_date = grade_transfer_change_date
                    to_be_modified.original_class = grade_transfer_original_class
                    to_be_modified.current_class = grade_transfer_current_class
                    to_be_modified.degrade_reason = grade_transfer_degrade_reason
                    to_be_modified.save()
                else:
                    message = 'Do not have the right of this operation'
            except: 
                try: # 如果用户是学生
                    request.session.get('user_type', 'Student')
                    authority = getAuthority('modify', 'GradeTransfer', 'Student', tag, user_id)
                    if authority:
                        to_be_modified.change_date = grade_transfer_change_date
                        to_be_modified.original_class = grade_transfer_original_class
                        to_be_modified.current_class = grade_transfer_current_class
                        to_be_modified.degrade_reason = grade_transfer_degrade_reason
                        to_be_modified.save()
                    else:
                        message = 'Do not have the right of this operation'
                except:
                    message = 'Please login'
            
        else:
            message = 'Please check out what you write'
    # 渲染动态页面
    grade_transfer_set = models.GradeTransfer.objects.all()
    show_result = []
    try: # 如果用户是老师
        request.session.get('user_type', 'Teacher')
        for result in grade_transfer_set: # 剔除所有结果中的非法结果
            authority = getAuthority('query', 'GradeTransfer', 'Teacher', result.student.student_id, user_id) # 检查用户对该元素的query权限
            if authority:
                show_result.append(result)
    except:
        try: # 如果用户是学生
            request.session.get('user_type', 'Student')
            for result in grade_transfer_set: # 剔除所有结果中的非法结果
                authority = getAuthority('query', 'GradeTransfer', 'Student', result.student.student_id, user_id) # 检查用户对该元素的query权限
                if authority:
                    show_result.append(result)
        except:
            message = 'Please login'
    grade_transfer_form = forms.GradeTransfer()
    grade_transfer_modify_form = forms.GradeTransfer_modify()
    return render(
        request,
        'manager/ManagePage/ManageGradeTransfer.html',
        {
            'grade_transfer_set' : grade_transfer_set,
            'grade_transfer_form' : grade_transfer_form,
            'modify_tag' : -1,
            'message' : message,
            'grade_transfer_modify_form' : grade_transfer_modify_form,
        }
    )

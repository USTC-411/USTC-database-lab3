# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.db.models import Q
from .. import forms
from .. import models
from manager.DataManage.authority import getAuthority

def teacher(request):
    modify_tag = -1
    message = ''
    show_result = []
    teacher_set = models.Teacher.objects.all()
    user_id = request.session['user_id']
    if request.GET.get('modify_tag'):
        modify_tag = request.GET.get('modify_tag')
    try: # 如果用户是老师
        request.session.get('user_type', 'Teacher')
        for result in teacher_set: # 剔除所有结果中的非法结果
            authority = getAuthority('query', 'Teacher', 'Teacher', result.id, user_id) # 检查用户对该元素的query权限
            if authority:
                show_result.append(result)
    except:
        try: # 如果用户是学生
            request.session.get('user_type', 'Student')
            for result in teacher_set: # 剔除所有结果中的非法结果
                authority = getAuthority('query', 'Teacher', 'Student', result.id, user_id) # 检查用户对该元素的query权限
                if authority:
                    show_result.append(result)
        except:
            message = 'Please login'
    teacher_form = forms.Teacher()
    teacher_modify_form = forms.Teacher_modify()
    return render(
        request,
        'manager/ManagePage/ManageTeacher.html',
        {
            'teacher_set' : show_result,
            'teacher_form' : teacher_form,
            'modify_tag' : modify_tag,
            'teacher_modify_form' : teacher_modify_form,
            'message': message,
        }
    )

def add(request):
    message = ''
    if request.method == 'POST':
        add_form = forms.Teacher(request.POST)
        print(add_form.errors)
        user_id = request.session['user_id']
        # 权限控制——这一部分用于判断账号类型，因为teacher只有管理员能操作，所以以下直接不允许相关操作
        if add_form.is_valid():
            teacher_id = add_form.cleaned_data.get('id')
            teacher_id_type = add_form.cleaned_data.get('id_type')
            teacher_name = add_form.cleaned_data.get('name')
            teacher_sex = add_form.cleaned_data.get('sex')
            teacher_birthday = add_form.cleaned_data.get('birthday')
            teacher_nationality = add_form.cleaned_data.get('nationality')
            teacher_family_address = add_form.cleaned_data.get('family_address')
            teacher_family_postcode = add_form.cleaned_data.get('family_postcode')
            teacher_family_telephone = add_form.cleaned_data.get('family_telephone')
            teacher_entry_date = add_form.cleaned_data.get('entry_date')
            teacher_email = add_form.cleaned_data.get('email')
            teacher_teacher_id = add_form.cleaned_data.get('teacher_id')
            teacher_password = add_form.cleaned_data.get('password')
            teacher_major = add_form.cleaned_data.get('major')
            teacher_title = add_form.cleaned_data.get('title')
            try: # 如果用户是老师
                request.session.get('user_type', 'Teacher')
                authority = getAuthority('add', 'Teacher', 'Teacher', teacher_id, user_id)
                if authority:
                    major = models.Major.objects.get(name=teacher_major)
                    new_teacher = models.Teacher.objects.create(
                        id = teacher_id,
                        id_type = teacher_id_type,
                        name = teacher_name,
                        sex = teacher_sex,
                        birthday = teacher_birthday,
                        nationality = teacher_nationality,
                        family_address = teacher_family_address,
                        family_postcode = teacher_family_postcode,
                        family_telephone = teacher_family_telephone,
                        entry_date = teacher_entry_date,
                        email = teacher_email,
                        teacher_id = teacher_teacher_id,
                        password = teacher_password,
                        major = major,
                        title = teacher_title,
                        isadmin = 0,
                    )
                else:
                    message = 'Do not have the right of this operation'
            except:
                try: # 如果用户是学生
                    request.session.get('user_type', 'Student')
                    authority = getAuthority('add', 'Teacher', 'Student', teacher_id, user_id)
                    if authority:
                        new_teacher = models.Teacher(
                            teacher_id,
                            teacher_id_type,
                            teacher_name,
                            teacher_sex,
                            teacher_birthday,
                            teacher_nationality,
                            teacher_family_address,
                            teacher_family_postcode,
                            teacher_family_telephone,
                            teacher_entry_date,
                            teacher_email,
                            teacher_teacher_id,
                            teacher_password,
                            teacher_major,
                            teacher_title,
                        )
                        new_teacher.save()
                    else:
                        message = 'Do not have the right of this operation'
                except:
                    message = 'Please login'
        else:
            message = "Please check what you've entered"
    # 渲染动态页面
    teacher_set = models.Teacher.objects.all()
    show_result = []
    try: # 如果用户是老师
        request.session.get('user_type', 'Teacher')
        for result in teacher_set: # 剔除所有结果中的非法结果
            authority = getAuthority('query', 'Teacher', 'Teacher', result.id, user_id) # 检查用户对该元素的query权限
            if authority:
                show_result.append(result)
    except:
        try: # 如果用户是学生
            request.session.get('user_type', 'Student')
            for result in teacher_set: # 剔除所有结果中的非法结果
                authority = getAuthority('query', 'Teacher', 'Student', result.id, user_id) # 检查用户对该元素的query权限
                if authority:
                    show_result.append(result)
        except:
            # message = 'Please login'
            pass
    teacher_form = forms.Teacher()
    teacher_modify_form = forms.Teacher_modify()
    return render(
        request,
        'manager/ManagePage/ManageTeacher.html',
        {
            'teacher_set' : show_result,
            'teacher_form' : teacher_form,
            'modify_tag' : -1,
            'teacher_modify_form' : teacher_modify_form,
            'message' : message
        }
    )

def delete(request):
    to_be_deleted_id = request.GET.get('id')
    to_be_deleted = models.Teacher.objects.get(id=to_be_deleted_id)
    user_id = request.session['user_id']
    message = ""
    try: # 如果用户是teacher
        request.session.get('user_type', 'Teacher')
        authority = getAuthority('delete', 'Teacher', 'Teacher', to_be_deleted_id, user_id)
        if authority:
            if to_be_deleted.ValidLesson.count() == 0 and to_be_deleted.HostClass.count() == 0:
                to_be_deleted.delete()
            else:
                message = "You cannot delete it, because it's referenced by others"
        else:
            message = 'Do not have the right of this operation'
    except:
        try: # 如果用户是student
            request.session.get('user_type', 'Student')
            authority = getAuthority('delete', 'Teacher', 'Student', to_be_deleted_id, user_id)
            if authority:
                if to_be_deleted.major.count() == 0:
                    to_be_deleted.delete()
                else:
                    message = "You cannot delete it, because it's referenced by others"
            else:
                message = 'Do not have the right of this operation'
        except:
            message = 'Please login'
    teacher_form = forms.Teacher()
    teacher_modify_form = forms.Teacher_modify()
    teacher_set = models.Teacher.objects.all()
    show_result = []
    try: # 如果用户是老师
        request.session.get('user_type', 'Teacher')
        for result in teacher_set: # 剔除所有结果中的非法结果
            authority = getAuthority('query', 'Teacher', 'Teacher', result.id, user_id) # 检查用户对该元素的query权限
            if authority:
                show_result.append(result)
    except:
        try: # 如果用户是学生
            request.session.get('user_type', 'Student')
            for result in teacher_set: # 剔除所有结果中的非法结果
                authority = getAuthority('query', 'Teacher', 'Student', result.id, user_id) # 检查用户对该元素的query权限
                if authority:
                    show_result.append(result)
        except:
            message = 'Please login'
    return render(
        request,
        'manager/ManagePage/ManageTeacher.html',
        {
            'teacher_set' : show_result,
            'teacher_form' : teacher_form,
            'modify_tag' : -1,
            'message': message,
            'teacher_modify_form' : teacher_modify_form,
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
                query_result = models.Teacher.objects.filter(id=query_val)
            elif option == 'id_type':
                query_result = models.Teacher.objects.filter(id_type=query_val)
            elif option == 'name':
                query_result = models.Teacher.objects.filter(name=query_val)
            elif option == 'sex':
                query_result = models.Teacher.objects.filter(sex=query_val)
            elif option == 'birthday':
                query_result = models.Teacher.objects.filter(birthday=query_val)
            elif option == 'nationality':
                query_result = models.Teacher.objects.filter(nationality=query_val)
            elif option == 'family_address':
                query_result = models.Teacher.objects.filter(family_address=query_val)
            elif option == 'family_postcode':
                query_result = models.Teacher.objects.filter(family_postcode=query_val)
            elif option == 'family_telephone':
                query_result = models.Teacher.objects.filter(family_telephone=query_val)
            elif option == 'entry_date':
                query_result = models.Teacher.objects.filter(entry_date=query_val)
            elif option == 'email':
                query_result = models.Teacher.objects.filter(email=query_val)
            elif option == 'teacher_id':
                query_result = models.Teacher.objects.filter(teacher_id=query_val)
            elif option == 'major':
                query_result = models.Teacher.objects.filter(major=query_val)
            elif option == 'title':
                query_result = models.Teacher.objects.filter(title=query_val)
            for result in query_result: # 剔除所有结果中的非法结果
                authority = getAuthority('query', 'Teacher', 'Teacher', result.id, user_id) # 检查用户对该元素的query权限
                if authority:
                    show_result.append(result)
        except:
            try: # 如果用户是student
                request.session.get('user_type', 'Student')
                if option == 'id': # 搜索所有结果，其中会有非法结果
                    query_result = models.Teacher.objects.filter(id=query_val)
                elif option == 'id_type':
                    query_result = models.Teacher.objects.filter(id_type=query_val)
                elif option == 'name':
                    query_result = models.Teacher.objects.filter(name=query_val)
                elif option == 'sex':
                    query_result = models.Teacher.objects.filter(sex=query_val)
                elif option == 'birthday':
                    query_result = models.Teacher.objects.filter(birthday=query_val)
                elif option == 'nationality':
                    query_result = models.Teacher.objects.filter(nationality=query_val)
                elif option == 'family_address':
                    query_result = models.Teacher.objects.filter(family_address=query_val)
                elif option == 'family_postcode':
                    query_result = models.Teacher.objects.filter(family_postcode=query_val)
                elif option == 'family_telephone':
                    query_result = models.Teacher.objects.filter(family_telephone=query_val)
                elif option == 'entry_date':
                    query_result = models.Teacher.objects.filter(entry_date=query_val)
                elif option == 'email':
                    query_result = models.Teacher.objects.filter(email=query_val)
                elif option == 'teacher_id':
                    query_result = models.Teacher.objects.filter(teacher_id=query_val)
                elif option == 'major':
                    query_result = models.Teacher.objects.filter(major=query_val)
                elif option == 'title':
                    query_result = models.Teacher.objects.filter(title=query_val)
                for result in query_result: # 剔除所有结果中的非法结果
                    authority = getAuthority('query', 'Teacher', 'Student', result.id, user_id) # 检查用户对该元素的query权限
                    if authority:
                        show_result.append(result)
            except:
                message = 'Please login'
        # 返回结果给页面
        teacher_form = forms.Teacher()
        teacher_modify_form = forms.Teacher_modify()
        return render(
            request,
            'manager/ManagePage/ManageTeacher.html',
            {
                'teacher_set' : show_result,
                'teacher_form' : teacher_form,
                'modify_tag' : -1,
                'teacher_modify_form' : teacher_modify_form,
            }
        )

def modify(request):
    if request.method == 'POST':
        modify_form = forms.Teacher_modify(request.POST)
        message = ''
        user_id = request.session['user_id']
        if modify_form.is_valid():
            teacher_id_type = modify_form.cleaned_data.get('id_type')
            teacher_name = modify_form.cleaned_data.get('name')
            teacher_sex = modify_form.cleaned_data.get('sex')
            teacher_birthday = modify_form.cleaned_data.get('birthday')
            teacher_nationality = modify_form.cleaned_data.get('nationality')
            teacher_family_address = modify_form.cleaned_data.get('family_address')
            teacher_family_postcode = modify_form.cleaned_data.get('family_postcode')
            teacher_family_telephone = modify_form.cleaned_data.get('family_telephone')
            teacher_entry_date = modify_form.cleaned_data.get('entry_date')
            teacher_email = modify_form.cleaned_data.get('email')
            teacher_password = modify_form.cleaned_data.get('password')
            teacher_major = modify_form.cleaned_data.get('major')
            teacher_title = modify_form.cleaned_data.get('title')
            tag = request.GET.get('tag')
            to_be_modified = models.Teacher.objects.get(id=tag)
            try: # 如果用户是老师
                request.session.get('user_type', 'Teacher')
                authority = getAuthority('modify', 'Teacher', 'Teacher', to_be_modified.teacher_id, user_id)
                if authority:
                    try:
                        to_be_modified.id_type = teacher_id_type
                        to_be_modified.name = teacher_name
                        to_be_modified.sex = teacher_sex
                        to_be_modified.birthday = teacher_birthday
                        to_be_modified.nationality = teacher_nationality
                        to_be_modified.family_address = teacher_family_address
                        to_be_modified.family_postcode = teacher_family_postcode
                        to_be_modified.family_telephone = teacher_family_telephone
                        to_be_modified.entry_date = teacher_entry_date
                        to_be_modified.email = teacher_email
                        to_be_modified.password = teacher_password
                        to_be_modified.major = teacher_major
                        to_be_modified.title = teacher_title
                        to_be_modified.save()
                    except:
                        print('testt')
                else:
                    message = 'Do not have the right of this operation'
            except: 
                try: # 如果用户是学生
                    request.session.get('user_type', 'Student')
                    authority = getAuthority('modify', 'Teacher', 'Student', tag, user_id)
                    if authority:
                        to_be_modified.id_type = teacher_id_type
                        to_be_modified.name = teacher_name
                        to_be_modified.sex = teacher_sex
                        to_be_modified.birthday = teacher_birthday
                        to_be_modified.nationality = teacher_nationality
                        to_be_modified.family_address = teacher_family_address
                        to_be_modified.family_postcode = teacher_family_postcode
                        to_be_modified.family_telephone = teacher_family_telephone
                        to_be_modified.entry_date = teacher_entry_date
                        to_be_modified.email = teacher_name
                        to_be_modified.password = teacher_password
                        to_be_modified.major = teacher_major
                        to_be_modified.title = teacher_title
                        to_be_modified.save()
                    else:
                        message = 'Do not have the right of this operation'
                except:
                    message = 'Please login'
            
        else:
            message = 'Please check out what you write'
    # 渲染动态页面
    teacher_set = models.Teacher.objects.all()
    show_result = []
    try: # 如果用户是老师
        request.session.get('user_type', 'Teacher')
        for result in teacher_set: # 剔除所有结果中的非法结果
            authority = getAuthority('query', 'Teacher', 'Teacher', result.id, user_id) # 检查用户对该元素的query权限
            if authority:
                show_result.append(result)
    except:
        try: # 如果用户是学生
            request.session.get('user_type', 'Student')
            for result in teacher_set: # 剔除所有结果中的非法结果
                authority = getAuthority('query', 'Teacher', 'Student', result.id, user_id) # 检查用户对该元素的query权限
                if authority:
                    show_result.append(result)
        except:
            message = 'Please login'
    teacher_form = forms.Teacher()
    teacher_modify_form = forms.Teacher_modify()
    return render(
        request,
        'manager/ManagePage/ManageTeacher.html',
        {
            'teacher_set' : teacher_set,
            'teacher_form' : teacher_form,
            'modify_tag' : -1,
            'message' : message,
            'teacher_modify_form' : teacher_modify_form,
        }
    )

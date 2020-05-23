# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.db.models import Q
from .. import forms
from .. import models
from manager.DataManage.authority import getAuthority

def student(request):
    modify_tag = -1
    message = ''
    show_result = []
    student_set = models.Student.objects.all()
    user_id = request.session['user_id']
    if request.GET.get('modify_tag'):
        modify_tag = request.GET.get('modify_tag')
    try: # 如果用户是老师
        request.session.get('user_type', 'Teacher')
        for result in student_set: # 剔除所有结果中的非法结果
            authority = getAuthority('query', 'Student', 'Teacher', result.id, user_id) # 检查用户对该元素的query权限
            if authority:
                show_result.append(result)
    except:
        try: # 如果用户是学生
            request.session.get('user_type', 'Student')
            for result in student_set: # 剔除所有结果中的非法结果
                authority = getAuthority('query', 'Student', 'Student', result.id, user_id) # 检查用户对该元素的query权限
                if authority:
                    show_result.append(result)
        except:
            message = 'Please login'
    student_form = forms.Student()
    student_modify_form = forms.Student_modify()
    return render(
        request,
        'manager/ManagePage/ManageStudent.html',
        {
            'student_set' : show_result,
            'student_form' : student_form,
            'modify_tag' : modify_tag,
            'student_modify_form' : student_modify_form,
            'message': message,
        }
    )

def add(request):
    message = ''
    if request.method == 'POST':
        add_form = forms.Student(request.POST)
        print(add_form.errors)
        user_id = request.session['user_id']
        # 权限控制——这一部分用于判断账号类型，因为student只有管理员能操作，所以以下直接不允许相关操作
        if add_form.is_valid():
            student_id = add_form.cleaned_data.get('id')
            student_id_type = add_form.cleaned_data.get('id_type')
            student_name = add_form.cleaned_data.get('name')
            student_sex = add_form.cleaned_data.get('sex')
            student_birthday = add_form.cleaned_data.get('birthday')
            student_nationality = add_form.cleaned_data.get('nationality')
            student_family_address = add_form.cleaned_data.get('family_address')
            student_family_postcode = add_form.cleaned_data.get('family_postcode')
            student_family_telephone = add_form.cleaned_data.get('family_telephone')
            student_entry_date = add_form.cleaned_data.get('entry_date')
            student_email = add_form.cleaned_data.get('email')
            student_student_id = add_form.cleaned_data.get('student_id')
            student_password = add_form.cleaned_data.get('password')
            student_myClass = add_form.cleaned_data.get('myClass')
            try: # 如果用户是老师
                request.session.get('user_type', 'Teacher')
                authority = getAuthority('add', 'Student', 'Teacher', student_id, user_id)
                if authority:
                    myClass = models.myClass.objects.get(name=student_myClass)
                    new_student = models.Student.objects.create(
                        id = student_id,
                        id_type = student_id_type,
                        name = student_name,
                        sex = student_sex,
                        birthday = student_birthday,
                        nationality = student_nationality,
                        family_address = student_family_address,
                        family_postcode = student_family_postcode,
                        family_telephone = student_family_telephone,
                        entry_date = student_entry_date,
                        email = student_email,
                        student_id = student_student_id,
                        password = student_password,
                        myClass = student_myClass,
                    )
                else:
                    message = 'Do not have the right of this operation'
            except:
                try: # 如果用户是学生
                    request.session.get('user_type', 'Teacher')
                    authority = getAuthority('add', 'Student', 'Teacher', student_id, user_id)
                    if authority:
                        new_student = models.Student(
                            student_id,
                            student_id_type,
                            student_name,
                            student_sex,
                            student_birthday,
                            student_nationality,
                            student_family_address,
                            student_family_postcode,
                            student_family_telephone,
                            student_entry_date,
                            student_email,
                            student_student_id,
                            student_password,
                            student_myClass,
                        )
                        new_student.save()
                    else:
                        message = 'Do not have the right of this operation'
                except:
                    message = 'Please login'
        else:
            message = "Please check what you've entered"
    # 渲染动态页面
    student_set = models.Student.objects.all()
    show_result = []
    try: # 如果用户是老师
        request.session.get('user_type', 'Teacher')
        for result in student_set: # 剔除所有结果中的非法结果
            authority = getAuthority('query', 'Student', 'Teacher', result.id, user_id) # 检查用户对该元素的query权限
            if authority:
                show_result.append(result)
    except:
        try: # 如果用户是学生
            request.session.get('user_type', 'Student')
            for result in student_set: # 剔除所有结果中的非法结果
                authority = getAuthority('query', 'Student', 'Student', result.id, user_id) # 检查用户对该元素的query权限
                if authority:
                    show_result.append(result)
        except:
            # message = 'Please login'
            pass
    student_form = forms.Student()
    student_modify_form = forms.Student_modify()
    return render(
        request,
        'manager/ManagePage/ManageStudent.html',
        {
            'student_set' : show_result,
            'student_form' : student_form,
            'modify_tag' : -1,
            'student_modify_form' : student_modify_form,
            'message' : message
        }
    )

def delete(request):
    to_be_deleted_id = request.GET.get('id')
    to_be_deleted = models.Student.objects.get(id=to_be_deleted_id)
    user_id = request.session['user_id']
    message = ""
    try: # 如果用户是student
        request.session.get('user_type', 'Teacher')
        authority = getAuthority('delete', 'Student', 'Teacher', to_be_deleted_id, user_id)
        if authority:
            try:
                to_be_deleted.major_transfer
                to_be_deleted.grade_transfer
                message = "You cannot delete it, because it's referenced by others"
            except:
                to_be_deleted.delete()
        else:
            message = 'Do not have the right of this operation'
    except:
        try: # 如果用户是student
            request.session.get('user_type', 'Student')
            authority = getAuthority('delete', 'Student', 'Student', to_be_deleted_id, user_id)
            if authority:
                try:
                    to_be_deleted.major_transfer
                    to_be_deleted.grade_transfer
                    message = "You cannot delete it, because it's referenced by others"
                except:
                    to_be_deleted.delete()
            else:
                message = 'Do not have the right of this operation'
        except:
            message = 'Please login'
    student_form = forms.Student()
    student_modify_form = forms.Student_modify()
    student_set = models.Student.objects.all()
    show_result = []
    try: # 如果用户是老师
        request.session.get('user_type', 'Teacher')
        for result in student_set: # 剔除所有结果中的非法结果
            authority = getAuthority('query', 'Student', 'Teacher', result.id, user_id) # 检查用户对该元素的query权限
            if authority:
                show_result.append(result)
    except:
        try: # 如果用户是学生
            request.session.get('user_type', 'Student')
            for result in student_set: # 剔除所有结果中的非法结果
                authority = getAuthority('query', 'Student', 'Student', result.id, user_id) # 检查用户对该元素的query权限
                if authority:
                    show_result.append(result)
        except:
            message = 'Please login'
    return render(
        request,
        'manager/ManagePage/ManageStudent.html',
        {
            'student_set' : show_result,
            'student_form' : student_form,
            'modify_tag' : -1,
            'message': message,
            'student_modify_form' : student_modify_form,
        }
    )

def query(request):
    show_result = [] # 这是最终展示给用户的搜索结果
    if  request.method == "GET":
        option = request.GET.get('option')
        query_val = request.GET.get('query_val')
        query_result = []
        user_id = request.session['user_id']
        try: # 如果用户是Teacher
            request.session.get('user_type', 'Teacher')
            if option == 'id': # 搜索所有结果，其中会有非法结果
                query_result = models.Student.objects.filter(id=query_val)
            elif option == 'id_type':
                query_result = models.Student.objects.filter(id_type=query_val)
            elif option == 'name':
                query_result = models.Student.objects.filter(name=query_val)
            elif option == 'sex':
                query_result = models.Student.objects.filter(sex=query_val)
            elif option == 'birthday':
                query_result = models.Student.objects.filter(birthday=query_val)
            elif option == 'nationality':
                query_result = models.Student.objects.filter(nationality=query_val)
            elif option == 'family_address':
                query_result = models.Student.objects.filter(family_address=query_val)
            elif option == 'family_postcode':
                query_result = models.Student.objects.filter(family_postcode=query_val)
            elif option == 'family_telephone':
                query_result = models.Student.objects.filter(family_telephone=query_val)
            elif option == 'entry_date':
                query_result = models.Student.objects.filter(entry_date=query_val)
            elif option == 'email':
                query_result = models.Student.objects.filter(email=query_val)
            elif option == 'student_id':
                query_result = models.Student.objects.filter(student_id=query_val)
            elif option == 'myClass':
                query_result = models.Student.objects.filter(myClass=query_val)
            for result in query_result: # 剔除所有结果中的非法结果
                authority = getAuthority('query', 'Student', 'Teacher', result.id, user_id) # 检查用户对该元素的query权限
                if authority:
                    show_result.append(result)
        except:
            try: # 如果用户是student
                request.session.get('user_type', 'Student')
                if option == 'id': # 搜索所有结果，其中会有非法结果
                    query_result = models.Student.objects.filter(id=query_val)
                elif option == 'id_type':
                    query_result = models.Student.objects.filter(id_type=query_val)
                elif option == 'name':
                    query_result = models.Student.objects.filter(name=query_val)
                elif option == 'sex':
                    query_result = models.Student.objects.filter(sex=query_val)
                elif option == 'birthday':
                    query_result = models.Student.objects.filter(birthday=query_val)
                elif option == 'nationality':
                    query_result = models.Student.objects.filter(nationality=query_val)
                elif option == 'family_address':
                    query_result = models.Student.objects.filter(family_address=query_val)
                elif option == 'family_postcode':
                    query_result = models.Student.objects.filter(family_postcode=query_val)
                elif option == 'family_telephone':
                    query_result = models.Student.objects.filter(family_telephone=query_val)
                elif option == 'entry_date':
                    query_result = models.Student.objects.filter(entry_date=query_val)
                elif option == 'email':
                    query_result = models.Student.objects.filter(email=query_val)
                elif option == 'student_id':
                    query_result = models.Student.objects.filter(student_id=query_val)
                elif option == 'myClass':
                    query_result = models.Student.objects.filter(myClass=query_val)
                for result in query_result: # 剔除所有结果中的非法结果
                    authority = getAuthority('query', 'Student', 'Student', result.id, user_id) # 检查用户对该元素的query权限
                    if authority:
                        show_result.append(result)
            except:
                message = 'Please login'
        # 返回结果给页面
        student_form = forms.Student()
        student_modify_form = forms.Student_modify()
        return render(
            request,
            'manager/ManagePage/ManageStudent.html',
            {
                'student_set' : show_result,
                'student_form' : student_form,
                'modify_tag' : -1,
                'student_modify_form' : student_modify_form,
            }
        )

def modify(request):
    if request.method == 'POST':
        modify_form = forms.Student_modify(request.POST)
        message = ''
        user_id = request.session['user_id']
        if modify_form.is_valid():
            student_id_type = modify_form.cleaned_data.get('id_type')
            student_name = modify_form.cleaned_data.get('name')
            student_sex = modify_form.cleaned_data.get('sex')
            student_birthday = modify_form.cleaned_data.get('birthday')
            student_nationality = modify_form.cleaned_data.get('nationality')
            student_family_address = modify_form.cleaned_data.get('family_address')
            student_family_postcode = modify_form.cleaned_data.get('family_postcode')
            student_family_telephone = modify_form.cleaned_data.get('family_telephone')
            student_entry_date = modify_form.cleaned_data.get('entry_date')
            student_email = modify_form.cleaned_data.get('email')
            student_password = modify_form.cleaned_data.get('password')
            student_myClass = modify_form.cleaned_data.get('myClass')
            tag = request.GET.get('tag')
            to_be_modified = models.Student.objects.get(id=tag)
            try: # 如果用户是老师
                request.session.get('user_type', 'Teacher')
                authority = getAuthority('modify', 'Student', 'Teacher', to_be_modified.student_id, user_id)
                if authority:
                    try:
                        to_be_modified.id_type = student_id_type
                        to_be_modified.name = student_name
                        to_be_modified.sex = student_sex
                        to_be_modified.birthday = student_birthday
                        to_be_modified.nationality = student_nationality
                        to_be_modified.family_address = student_family_address
                        to_be_modified.family_postcode = student_family_postcode
                        to_be_modified.family_telephone = student_family_telephone
                        to_be_modified.entry_date = student_entry_date
                        to_be_modified.email = student_email
                        to_be_modified.password = student_password
                        to_be_modified.myClass = student_myClass
                        to_be_modified.save()
                    except:
                        print('testt')
                else:
                    message = 'Do not have the right of this operation'
            except: 
                try: # 如果用户是学生
                    request.session.get('user_type', 'Student')
                    authority = getAuthority('modify', 'Student', 'Student', tag, user_id)
                    if authority:
                        to_be_modified.id_type = student_id_type
                        to_be_modified.name = student_name
                        to_be_modified.sex = student_sex
                        to_be_modified.birthday = student_birthday
                        to_be_modified.nationality = student_nationality
                        to_be_modified.family_address = student_family_address
                        to_be_modified.family_postcode = student_family_postcode
                        to_be_modified.family_telephone = student_family_telephone
                        to_be_modified.entry_date = student_entry_date
                        to_be_modified.email = student_name
                        to_be_modified.password = student_password
                        to_be_modified.myClass = student_myClass
                        to_be_modified.save()
                    else:
                        message = 'Do not have the right of this operation'
                except:
                    message = 'Please login'
            
        else:
            message = 'Please check out what you write'
    # 渲染动态页面
    student_set = models.Student.objects.all()
    show_result = []
    try: # 如果用户是老师
        request.session.get('user_type', 'Student')
        for result in student_set: # 剔除所有结果中的非法结果
            authority = getAuthority('query', 'Student', 'Teacher', result.id, user_id) # 检查用户对该元素的query权限
            if authority:
                show_result.append(result)
    except:
        try: # 如果用户是学生
            request.session.get('user_type', 'Student')
            for result in student_set: # 剔除所有结果中的非法结果
                authority = getAuthority('query', 'Student', 'Teacher', result.id, user_id) # 检查用户对该元素的query权限
                if authority:
                    show_result.append(result)
        except:
            message = 'Please login'
    student_form = forms.Student()
    student_modify_form = forms.Student_modify()
    return render(
        request,
        'manager/ManagePage/ManageStudent.html',
        {
            'student_set' : student_set,
            'student_form' : student_form,
            'modify_tag' : -1,
            'message' : message,
            'student_modify_form' : student_modify_form,
        }
    )

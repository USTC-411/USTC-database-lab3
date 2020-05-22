from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.db.models import Q
from .. import forms
from .. import models
from manager.DataManage.authority import getAuthority

def major(request):
    modify_tag = -1
    message = ''
    show_result = []
    major_set = models.Major.objects.all()
    user_id = request.session['user_id']
    if request.GET.get('modify_tag'):
        modify_tag = request.GET.get('modify_tag')
    try: # 如果用户是老师
        request.session.get('user_type', 'Teacher')
        for result in major_set: # 剔除所有结果中的非法结果
            authority = getAuthority('query', 'Major', 'Teacher', result.id, user_id) # 检查用户对该元素的query权限
            if authority:
                show_result.append(result)
    except:
        try: # 如果用户是学生
            request.session.get('user_type', 'Student')
            for result in major_set: # 剔除所有结果中的非法结果
                authority = getAuthority('query', 'Major', 'Student', result.id, user_id) # 检查用户对该元素的query权限
                if authority:
                    show_result.append(result)
        except:
            message = 'Please login'
    major_form = forms.Major()
    major_modify_form = forms.Major_modify()
    return render(
        request,
        'manager/ManagePage/ManageMajor.html',
        {
            'major_set' : show_result,
            'major_form' : major_form,
            'modify_tag' : modify_tag,
            'major_modify_form' : major_modify_form,
            'message': message,
        }
    )

def add(request):
    message = ''
    if request.method == 'POST':
        add_form = forms.Major(request.POST)
        user_id = request.session['user_id']
        # 权限控制——这一部分用于判断账号类型，因为major只有管理员能操作，所以以下直接不允许相关操作
        if add_form.is_valid():
            major_id = add_form.cleaned_data.get('id')
            major_name = add_form.cleaned_data.get('name')
            major_address = add_form.cleaned_data.get('address')
            major_principal = add_form.cleaned_data.get('address')
            major_campus = add_form.cleaned_data.get('campus')
            try: # 如果用户是老师
                request.session.get('user_type', 'Teacher')
                authority = getAuthority('add', 'Major', 'Teacher', major_id, user_id)
                if authority:
                    new_major = models.Major(major_id, major_name, major_address,major_principal,major_campus)
                    new_major.save()
                else:
                    message = 'Do not have the right of this operation'
            except:
                try: # 如果用户是学生
                    request.session.get('user_type', 'Student')
                    authority = getAuthority('add', 'Major', 'Student', major_id, user_id)
                    if authority:
                        new_major = models.Major(major_id, major_name, major_address, major_principal, major_campus)
                        new_major.save()
                    else:
                        message = 'Do not have the right of this operation'
                except:
                    message = 'Please login'
        else:
            message = "Please check what you've entered"
    # 渲染动态页面
    major_set = models.Major.objects.all()
    show_result = []
    try: # 如果用户是老师
        request.session.get('user_type', 'Teacher')
        for result in major_set: # 剔除所有结果中的非法结果
            authority = getAuthority('query', 'Major', 'Teacher', result.id, user_id) # 检查用户对该元素的query权限
            if authority:
                show_result.append(result)
    except:
        try: # 如果用户是学生
            request.session.get('user_type', 'Student')
            for result in major_set: # 剔除所有结果中的非法结果
                authority = getAuthority('query', 'Major', 'Student', result.id, user_id) # 检查用户对该元素的query权限
                if authority:
                    show_result.append(result)
        except:
            message = 'Please login'
    major_form = forms.Major()
    major_modify_form = forms.Major_modify()
    return render(
        request,
        'manager/ManagePage/ManageMajor.html',
        {
            'major_set' : show_result,
            'major_form' : major_form,
            'modify_tag' : -1,
            'major_modify_form' : major_modify_form,
            'message' : message
        }
    )

def delete(request):
    to_be_deleted_id = request.GET.get('id')
    to_be_deleted = models.Major.objects.get(id=to_be_deleted_id)
    user_id = request.session['user_id']
    message = ""
    try: # 如果用户是teacher
        request.session.get('user_type', 'Teacher')
        authority = getAuthority('delete', 'Major', 'Teacher', to_be_deleted_id, user_id)
        if authority:
            if to_be_deleted.major.count() == 0:
                to_be_deleted.delete()
            else:
                message = "You cannot delete it, because it's referenced by others"
        else:
            message = 'Do not have the right of this operation'
    except:
        try: # 如果用户是student
            request.session.get('user_type', 'Student')
            authority = getAuthority('delete', 'Major', 'Student', to_be_deleted_id, user_id)
            if authority:
                if to_be_deleted.major.count() == 0:
                    to_be_deleted.delete()
                else:
                    message = "You cannot delete it, because it's referenced by others"
            else:
                message = 'Do not have the right of this operation'
        except:
            message = 'Please login'
    major_form = forms.Major()
    major_modify_form = forms.Major_modify()
    major_set = models.Major.objects.all()
    show_result = []
    try: # 如果用户是老师
        request.session.get('user_type', 'Teacher')
        for result in major_set: # 剔除所有结果中的非法结果
            authority = getAuthority('query', 'Major', 'Teacher', result.id, user_id) # 检查用户对该元素的query权限
            if authority:
                show_result.append(result)
    except:
        try: # 如果用户是学生
            request.session.get('user_type', 'Student')
            for result in major_set: # 剔除所有结果中的非法结果
                authority = getAuthority('query', 'Major', 'Student', result.id, user_id) # 检查用户对该元素的query权限
                if authority:
                    show_result.append(result)
        except:
            message = 'Please login'
    return render(
        request,
        'manager/ManagePage/ManageMajor.html',
        {
            'major_set' : show_result,
            'major_form' : major_form,
            'modify_tag' : -1,
            'message': message,
            'major_modify_form' : major_modify_form,
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
                query_result = models.Major.objects.filter(id=query_val)
            elif option == 'name':
                query_result = models.Major.objects.filter(name=query_val)
            elif option == 'address':
                query_result = models.Major.objects.filter(address=query_val)
            elif option == 'principal':
                query_result = models.Major.objects.filter(principal=query_val)
            elif option == 'campus':
                query_result = models.Major.objects.filter(campus=query_val)
            for result in query_result: # 剔除所有结果中的非法结果
                authority = getAuthority('query', 'Major', 'Teacher', result.id, user_id) # 检查用户对该元素的query权限
                if authority:
                    show_result.append(result)
        except:
            try: # 如果用户是student
                request.session.get('user_type', 'Student')
                if option == 'id': # 搜索所有结果，其中会有非法结果
                    query_result = models.Major.objects.filter(id=query_val)
                elif option == 'name':
                    query_result = models.Major.objects.filter(name=query_val)
                elif option == 'address':
                    query_result = models.Major.objects.filter(address=query_val)
                elif option == 'principal':
                    query_result = models.Major.objects.filter(principal=query_val)
                elif option == 'campus':
                    query_result = models.Major.objects.filter(campus=query_val)
                for result in query_result: # 剔除所有结果中的非法结果
                    authority = getAuthority('query', 'Major', 'Student', result.id, user_id) # 检查用户对该元素的query权限
                    if authority:
                        show_result.append(result)
            except:
                message = 'Please login'
        # 返回结果给页面
        major_form = forms.Major()
        major_modify_form = forms.Major_modify()
        return render(
            request,
            'manager/ManagePage/ManageMajor.html',
            {
                'major_set' : show_result,
                'major_form' : major_form,
                'modify_tag' : -1,
                'major_modify_form' : major_modify_form,
            }
        )

def modify(request):
    if request.method == 'POST':
        modify_form = forms.Major_modify(request.POST)
        message = ''
        user_id = request.session['user_id']
        if modify_form.is_valid():
            major_name = modify_form.cleaned_data.get('name')
            major_address = modify_form.cleaned_data.get('address')
            major_principal = modify_form.cleaned_data.get('principal')
            major_campus = modify_form.cleaned_data.get('campus')
            tag = request.GET.get('tag')
            to_be_modified = models.Major.objects.get(id=tag)
            try: # 如果用户是老师
                request.session.get('user_type', 'Teacher')
                authority = getAuthority('modify', 'Major', 'Teacher', tag, user_id)
                if authority:
                    to_be_modified.name = major_name
                    to_be_modified.address = major_address
                    to_be_modified.principal = major_principal
                    to_be_modified.campus = major_campus
                    to_be_modified.save()
                else:
                    message = 'Do not have the right of this operation'
            except: 
                try: # 如果用户是学生
                    request.session.get('user_type', 'Student')
                    authority = getAuthority('modify', 'Major', 'Student', tag, user_id)
                    if authority:
                        to_be_modified.name = major_name
                        to_be_modified.address = major_address
                        to_be_modified.principal = major_principal
                        to_be_modified.campus = major_campus
                        to_be_modified.save()
                    else:
                        message = 'Do not have the right of this operation'
                except:
                    message = 'Please login'
            
        else:
            message = 'Please check out what you write'
    # 渲染动态页面
    major_set = models.Major.objects.all()
    show_result = []
    try: # 如果用户是老师
        request.session.get('user_type', 'Teacher')
        for result in major_set: # 剔除所有结果中的非法结果
            authority = getAuthority('query', 'Major', 'Teacher', result.id, user_id) # 检查用户对该元素的query权限
            if authority:
                show_result.append(result)
    except:
        try: # 如果用户是学生
            request.session.get('user_type', 'Student')
            for result in major_set: # 剔除所有结果中的非法结果
                authority = getAuthority('query', 'Major', 'Student', result.id, user_id) # 检查用户对该元素的query权限
                if authority:
                    show_result.append(result)
        except:
            message = 'Please login'
    major_form = forms.Major()
    major_modify_form = forms.Major_modify()
    return render(
        request,
        'manager/ManagePage/ManageMajor.html',
        {
            'major_set' : major_set,
            'major_form' : major_form,
            'modify_tag' : -1,
            'message' : message,
            'major_modify_form' : major_modify_form,
        }
    )

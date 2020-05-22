# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.db.models import Q
from .. import forms
from .. import models
from manager.DataManage.authority import getAuthority

def campus(request):
    modify_tag = -1
    message = ''
    show_result = []
    campus_set = models.Campus.objects.all()
    user_id = request.session['user_id']
    if request.GET.get('modify_tag'):
        modify_tag = request.GET.get('modify_tag')
    try: # 如果用户是老师
        request.session.get('user_type', 'Teacher')
        for result in campus_set: # 剔除所有结果中的非法结果
            authority = getAuthority('query', 'Campus', 'Teacher', result.id, user_id) # 检查用户对该元素的query权限
            if authority:
                show_result.append(result)
    except:
        try: # 如果用户是学生
            request.session.get('user_type', 'Student')
            for result in campus_set: # 剔除所有结果中的非法结果
                authority = getAuthority('query', 'Campus', 'Student', result.id, user_id) # 检查用户对该元素的query权限
                if authority:
                    show_result.append(result)
        except:
            message = 'Please login'
    campus_form = forms.Campus()
    campus_modify_form = forms.Campus_modify()
    return render(
        request,
        'manager/ManagePage/ManageCampus.html',
        {
            'campus_set' : show_result,
            'campus_form' : campus_form,
            'modify_tag' : modify_tag,
            'campus_modify_form' : campus_modify_form,
            'message': message,
        }
    )

def add(request):
    message = ''
    if request.method == 'POST':
        add_form = forms.Campus(request.POST)
        user_id = request.session['user_id']
        # 权限控制——这一部分用于判断账号类型，因为campus只有管理员能操作，所以以下直接不允许相关操作
        if add_form.is_valid():
            campus_id = add_form.cleaned_data.get('id')
            campus_name = add_form.cleaned_data.get('name')
            campus_address = add_form.cleaned_data.get('address')
            try: # 如果用户是老师
                request.session.get('user_type', 'Teacher')
                authority = getAuthority('add', 'Campus', 'Teacher', campus_id, user_id)
                if authority:
                    new_campus = models.Campus(campus_id, campus_name, campus_address)
                    new_campus.save()
                else:
                    message = 'Do not have the right of this operation'
            except:
                try: # 如果用户是学生
                    request.session.get('user_type', 'Student')
                    authority = getAuthority('add', 'Campus', 'Student', campus_id, user_id)
                    if authority:
                        new_campus = models.Campus(campus_id, campus_name, campus_address)
                        new_campus.save()
                    else:
                        message = 'Do not have the right of this operation'
                except:
                    message = 'Please login'
        else:
            message = "Please check what you've entered"
    # 渲染动态页面
    campus_set = models.Campus.objects.all()
    show_result = []
    try: # 如果用户是老师
        request.session.get('user_type', 'Teacher')
        for result in campus_set: # 剔除所有结果中的非法结果
            authority = getAuthority('query', 'Campus', 'Teacher', result.id, user_id) # 检查用户对该元素的query权限
            if authority:
                show_result.append(result)
    except:
        try: # 如果用户是学生
            request.session.get('user_type', 'Student')
            for result in campus_set: # 剔除所有结果中的非法结果
                authority = getAuthority('query', 'Campus', 'Student', result.id, user_id) # 检查用户对该元素的query权限
                if authority:
                    show_result.append(result)
        except:
            message = 'Please login'
    campus_form = forms.Campus()
    campus_modify_form = forms.Campus_modify()
    return render(
        request,
        'manager/ManagePage/ManageCampus.html',
        {
            'campus_set' : show_result,
            'campus_form' : campus_form,
            'modify_tag' : -1,
            'campus_modify_form' : campus_modify_form,
            'message' : message
        }
    )

def delete(request):
    to_be_deleted_id = request.GET.get('id')
    to_be_deleted = models.Campus.objects.get(id=to_be_deleted_id)
    user_id = request.session['user_id']
    message = ""
    try: # 如果用户是teacher
        request.session.get('user_type', 'Teacher')
        authority = getAuthority('delete', 'Campus', 'Teacher', to_be_deleted_id, user_id)
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
            authority = getAuthority('delete', 'Campus', 'Student', to_be_deleted_id, user_id)
            if authority:
                if to_be_deleted.major.count() == 0:
                    to_be_deleted.delete()
                else:
                    message = "You cannot delete it, because it's referenced by others"
            else:
                message = 'Do not have the right of this operation'
        except:
            message = 'Please login'
    campus_form = forms.Campus()
    campus_modify_form = forms.Campus_modify()
    campus_set = models.Campus.objects.all()
    show_result = []
    try: # 如果用户是老师
        request.session.get('user_type', 'Teacher')
        for result in campus_set: # 剔除所有结果中的非法结果
            authority = getAuthority('query', 'Campus', 'Teacher', result.id, user_id) # 检查用户对该元素的query权限
            if authority:
                show_result.append(result)
    except:
        try: # 如果用户是学生
            request.session.get('user_type', 'Student')
            for result in campus_set: # 剔除所有结果中的非法结果
                authority = getAuthority('query', 'Campus', 'Student', result.id, user_id) # 检查用户对该元素的query权限
                if authority:
                    show_result.append(result)
        except:
            message = 'Please login'
    return render(
        request,
        'manager/ManagePage/ManageCampus.html',
        {
            'campus_set' : show_result,
            'campus_form' : campus_form,
            'modify_tag' : -1,
            'message': message,
            'campus_modify_form' : campus_modify_form,
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
                query_result = models.Campus.objects.filter(id=query_val)
            elif option == 'name':
                query_result = models.Campus.objects.filter(name=query_val)
            elif option == 'address':
                query_result = models.Campus.objects.filter(address=query_val)
            for result in query_result: # 剔除所有结果中的非法结果
                authority = getAuthority('query', 'Campus', 'Teacher', result.id, user_id) # 检查用户对该元素的query权限
                if authority:
                    show_result.append(result)
        except:
            try: # 如果用户是student
                request.session.get('user_type', 'Student')
                if option == 'id': # 搜索所有结果，其中会有非法结果
                    query_result = models.Campus.objects.filter(id=query_val)
                elif option == 'name':
                    query_result = models.Campus.objects.filter(name=query_val)
                elif option == 'address':
                    query_result = models.Campus.objects.filter(address=query_val)
                for result in query_result: # 剔除所有结果中的非法结果
                    authority = getAuthority('query', 'Campus', 'Student', result.id, user_id) # 检查用户对该元素的query权限
                    if authority:
                        show_result.append(result)
            except:
                message = 'Please login'
        # 返回结果给页面
        campus_form = forms.Campus()
        campus_modify_form = forms.Campus_modify()
        return render(
            request,
            'manager/ManagePage/ManageCampus.html',
            {
                'campus_set' : show_result,
                'campus_form' : campus_form,
                'modify_tag' : -1,
                'campus_modify_form' : campus_modify_form,
            }
        )

def modify(request):
    if request.method == 'POST':
        modify_form = forms.Campus_modify(request.POST)
        message = ''
        user_id = request.session['user_id']
        if modify_form.is_valid():
            campus_name = modify_form.cleaned_data.get('name')
            campus_address = modify_form.cleaned_data.get('address')
            tag = request.GET.get('tag')
            to_be_modified = models.Campus.objects.get(id=tag)
            try: # 如果用户是老师
                request.session.get('user_type', 'Teacher')
                authority = getAuthority('modify', 'Campus', 'Teacher', tag, user_id)
                if authority:
                    to_be_modified.name = campus_name
                    to_be_modified.address = campus_address
                    to_be_modified.save()
                else:
                    message = 'Do not have the right of this operation'
            except: 
                try: # 如果用户是学生
                    request.session.get('user_type', 'Student')
                    authority = getAuthority('modify', 'Campus', 'Student', tag, user_id)
                    if authority:
                        to_be_modified.name = campus_name
                        to_be_modified.address = campus_address
                        to_be_modified.save()
                    else:
                        message = 'Do not have the right of this operation'
                except:
                    message = 'Please login'
            
        else:
            message = 'Please check out what you write'
    # 渲染动态页面
    campus_set = models.Campus.objects.all()
    show_result = []
    try: # 如果用户是老师
        request.session.get('user_type', 'Teacher')
        for result in campus_set: # 剔除所有结果中的非法结果
            authority = getAuthority('query', 'Campus', 'Teacher', result.id, user_id) # 检查用户对该元素的query权限
            if authority:
                show_result.append(result)
    except:
        try: # 如果用户是学生
            request.session.get('user_type', 'Student')
            for result in campus_set: # 剔除所有结果中的非法结果
                authority = getAuthority('query', 'Campus', 'Student', result.id, user_id) # 检查用户对该元素的query权限
                if authority:
                    show_result.append(result)
        except:
            message = 'Please login'
    campus_form = forms.Campus()
    campus_modify_form = forms.Campus_modify()
    return render(
        request,
        'manager/ManagePage/ManageCampus.html',
        {
            'campus_set' : campus_set,
            'campus_form' : campus_form,
            'modify_tag' : -1,
            'message' : message,
            'campus_modify_form' : campus_modify_form,
        }
    )

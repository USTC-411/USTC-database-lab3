from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.db.models import Q
from .. import forms
from .. import models
from manager.DataManage.authority import getAuthority

def classes(request):
    modify_tag = -1
    message = ''
    show_result = []
    class_set = models.myClass.objects.all()
    user_id = request.session['user_id']
    if request.GET.get('modify_tag'):
        modify_tag = request.GET.get('modify_tag')
    try: # 如果用户是老师
        request.session.get('user_type', 'Teacher')
        for result in class_set: # 剔除所有结果中的非法结果
            authority = getAuthority('query', 'Class', 'Teacher', result.id, user_id) # 检查用户对该元素的query权限
            if authority:
                show_result.append(result)
    except:
        try: # 如果用户是学生
            request.session.get('user_type', 'Student')
            for result in class_set: # 剔除所有结果中的非法结果
                authority = getAuthority('query', 'Class', 'Student', result.id, user_id) # 检查用户对该元素的query权限
                if authority:
                    show_result.append(result)
        except:
            message = 'Please login'
            #message = request.session['user_type']
    
    class_form = forms.myClass()
    class_modify_form = forms.myClass_modify()
    return render(
        request,
        'manager/ManagePage/ManageClass.html',
        {
            'class_set' : show_result,
            'class_form' : class_form,
            'modify_tag' : modify_tag,
            'class_modify_form' : class_modify_form,
            'message': message,
        }
    )

def add(request):
    message = ''
    if request.method == 'POST':
        add_form = forms.myClass(request.POST)
        #print(add_form.cleaned_data.get('id'))
        print(add_form.errors)
        user_id = request.session['user_id']
        # 权限控制——这一部分用于判断账号类型，因为campus只有管理员能操作，所以以下直接不允许相关操作
        if add_form.is_valid():
            class_id = add_form.cleaned_data.get('id')
            class_name = add_form.cleaned_data.get('name')
            set_up_date = add_form.cleaned_data.get('date')
            head_teacher = add_form.cleaned_data.get('head_teacher')
            grade = add_form.cleaned_data.get('grade')
            class_major = add_form.cleaned_data.get('major')
            print(class_major)
            #try: # 如果用户是老师
            request.session.get('user_type', 'Teacher')
            authority = getAuthority('add', 'Class', 'Teacher', class_id, user_id)
            if authority:
                class_major_in = models.Major.objects.get(name = class_major)
                class_teacher_in = models.Teacher.objects.get(name = head_teacher)
                new_class = models.myClass(class_id, class_name, set_up_date,head_teacher=class_teacher_in,grade=grade,major=class_major_in)
                new_class.save()
            else:
                message = 'Do not have the right of this operation'
            '''except:
                try: # 如果用户是学生
                    request.session.get('user_type', 'Student')
                    authority = getAuthority('add', 'Class', 'Student', campus_id, user_id)
                    if authority:
                        new_campus = models.myClass(class_id, class_name, set_up_date,head_teacher,grade,major)
                        new_campus.save()
                    else:
                        message = 'Do not have the right of this operation'
                except:
                    message = 'Please login' '''
        else:
            message = "Please check what you've entered"
    # 渲染动态页面
    class_set = models.myClass.objects.all()
    show_result = []
    try: # 如果用户是老师
        request.session.get('user_type', 'Teacher')
        for result in class_set: # 剔除所有结果中的非法结果
            authority = getAuthority('query', 'Class', 'Teacher', result.id, user_id) # 检查用户对该元素的query权限
            if authority:
                show_result.append(result)
    except:
        try: # 如果用户是学生
            request.session.get('user_type', 'Student')
            for result in class_set: # 剔除所有结果中的非法结果
                authority = getAuthority('query', 'Class', 'Student', result.id, user_id) # 检查用户对该元素的query权限
                if authority:
                    show_result.append(result)
        except:
            message = 'Please login'
    class_form = forms.myClass()
    class_modify_form = forms.myClass_modify()
    return render(
        request,
        'manager/ManagePage/ManageClass.html',
        {
            'class_set' : show_result,
            'class_form' : class_form,
            'modify_tag' : -1,
            'class_modify_form' : class_modify_form,
            'message' : message
        }
    )

def delete(request): 
    to_be_deleted_id = request.GET.get('id')
    to_be_deleted = models.myClass.objects.get(id=to_be_deleted_id)
    user_id = request.session['user_id']
    message = ""
    try: # 如果用户是teacher
        request.session.get('user_type', 'Teacher')
        authority = getAuthority('delete', 'Class', 'Teacher', to_be_deleted_id, user_id)
        if authority:
            if to_be_deleted.students.count() == 0:
                to_be_deleted.delete()
            else:
                message = "You cannot delete it, because it's referenced by others"
        else:
            message = 'Do not have the right of this operation'
    except:
        try: # 如果用户是student
            request.session.get('user_type', 'Student')
            authority = getAuthority('delete', 'Class', 'Student', to_be_deleted_id, user_id)
            if authority:
                if to_be_deleted.students.count() == 0:
                    to_be_deleted.delete()
                else:
                    message = "You cannot delete it, because it's referenced by others"
            else:
                message = 'Do not have the right of this operation'
        except:
            message = 'Please login'
    class_form = forms.myClass()
    class_modify_form = forms.myClass_modify()
    class_set = models.myClass.objects.all()
    show_result = []
    try: # 如果用户是老师
        request.session.get('user_type', 'Teacher')
        for result in class_set: # 剔除所有结果中的非法结果
            authority = getAuthority('query', 'Class', 'Teacher', result.id, user_id) # 检查用户对该元素的query权限
            if authority:
                show_result.append(result)
    except:
        try: # 如果用户是学生
            request.session.get('user_type', 'Student')
            for result in class_set: # 剔除所有结果中的非法结果
                authority = getAuthority('query', 'Class', 'Student', result.id, user_id) # 检查用户对该元素的query权限
                if authority:
                    show_result.append(result)
        except:
            message = 'Please login'
    return render(
        request,
        'manager/ManagePage/ManageClass.html',
        {
            'class_set' : show_result,
            'class_form' : class_form,
            'modify_tag' : -1,
            'message': message,
            'class_modify_form' : class_modify_form,
        }
    )


'''def delete(request):
    to_be_deleted_id = request.GET.get('id')
    to_be_deleted = models.Major.objects.get(id=to_be_deleted_id)
    user_id = request.session['user_id']
    message = ""
    try: # 如果用户是teacher
        request.session.get('user_type', 'Teacher')
        authority = getAuthority('delete', 'Major', 'Teacher', to_be_deleted_id, user_id)
        if authority:
            if to_be_deleted.Lesson.count() == 0 and to_be_deleted.Teacher.count() == 0 and to_be_deleted.myClass.count() == 0:
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
                if to_be_deleted.Lesson.count() == 0 and to_be_deleted.Teacher.count() == 0 and to_be_deleted.myClass.count() == 0:
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
    )'''

'''def query(request):
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
        )'''
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
                query_result = models.myClass.objects.filter(id=query_val)
            elif option == 'name':
                query_result = models.myClass.objects.filter(name=query_val)
            elif option == 'date':
                query_result = models.myClass.objects.filter(date=query_val)
            elif option == 'head_teacher':
                query_result = models.myClass.objects.filter(head_teacher=query_val)
            elif option == 'grade':
                query_result = models.myClass.objects.filter(grade=query_val)
            elif option == 'major':
                query_result = models.myClass.objects.filter(major=query_val)
            for result in query_result: # 剔除所有结果中的非法结果
                authority = getAuthority('query', 'Class', 'Teacher', result.id, user_id) # 检查用户对该元素的query权限
                if authority:
                    show_result.append(result)
        except:
            try: # 如果用户是student
                request.session.get('user_type', 'Student')
                if option == 'id': # 搜索所有结果，其中会有非法结果
                    query_result = models.myClass.objects.filter(id=query_val)
                elif option == 'name':
                    query_result = models.myClass.objects.filter(name=query_val)
                elif option == 'date':
                    query_result = models.myClass.objects.filter(date=query_val)
                elif option == 'head_teacher':
                    query_result = models.myClass.objects.filter(head_teacher=query_val)
                elif option == 'grade':
                    query_result = models.myClass.objects.filter(grade=query_val)
                elif option == 'major':
                    query_result = models.myClass.objects.filter(major=query_val)
                for result in query_result: # 剔除所有结果中的非法结果
                    authority = getAuthority('query', 'Class', 'Student', result.id, user_id) # 检查用户对该元素的query权限
                    if authority:
                        show_result.append(result)
            except:
                message = 'Please login'
        # 返回结果给页面
        class_form = forms.myClass()
        class_modify_form = forms.myClass_modify()
        return render(
            request,
            'manager/ManagePage/ManageClass.html',
            {
                'class_set' : show_result,
                'class_form' : class_form,
                'modify_tag' : -1,
                'message' : message,
                'class_modify_form' : class_modify_form,
            }
        )

def modify(request):
    if request.method == 'POST':
        modify_form = forms.myClass_modify(request.POST)
        message = ''
        user_id = request.session['user_id']
        if modify_form.is_valid():
            class_name = modify_form.cleaned_data.get('name')
            class_date = modify_form.cleaned_data.get('date')
            head_teacher = modify_form.cleaned_data.get('head_teacher')
            class_grade = modify_form.cleaned_data.get('grade')
            tag = request.GET.get('tag')
            to_be_modified = models.myClass.objects.get(id=tag)
            try: # 如果用户是老师
                request.session.get('user_type', 'Teacher')
                authority = getAuthority('modify', 'Class', 'Teacher', tag, user_id)
                if authority:
                    to_be_modified.name = class_name
                    to_be_modified.date = class_date
                    to_be_modified.head_teacher = head_teacher
                    to_be_modified.grade = class_grade
                    to_be_modified.save()
                else:
                    message = 'Do not have the right of this operation'
            except: 
                try: # 如果用户是学生
                    request.session.get('user_type', 'Student')
                    authority = getAuthority('modify', 'Class', 'Student', tag, user_id)
                    if authority:
                        to_be_modified.name = class_name
                        to_be_modified.date = class_date
                        to_be_modified.head_teacher = head_teacher
                        to_be_modified.grade = class_grade
                        to_be_modified.save()
                    else:
                        message = 'Do not have the right of this operation'
                except:
                    message = 'Please login'
            
        else:
            message = 'Please check out what you write'
    # 渲染动态页面
    class_set = models.myClass.objects.all()
    show_result = []
    try: # 如果用户是老师
        request.session.get('user_type', 'Teacher')
        for result in class_set: # 剔除所有结果中的非法结果
            authority = getAuthority('query', 'Class', 'Teacher', result.id, user_id) # 检查用户对该元素的query权限
            if authority:
                show_result.append(result)
    except:
        try: # 如果用户是学生
            request.session.get('user_type', 'Student')
            for result in class_set: # 剔除所有结果中的非法结果
                authority = getAuthority('query', 'Class', 'Student', result.id, user_id) # 检查用户对该元素的query权限
                if authority:
                    show_result.append(result)
        except:
            message = 'Please login'
    class_form = forms.myClass()
    class_modify_form = forms.myClass_modify()
    return render(
        request,
        'manager/ManagePage/ManageClass.html',
        {
            'class_set' : class_set,
            'class_form' : class_form,
            'modify_tag' : -1,
            'message' : message,
            'class_modify_form' : class_modify_form,
        }
    )

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from . import models

# Create your views here.
def IndexForStudent(request):
    return render(request, 'manager/IndexForStudent.html')

def IndexForTeacher(request):
    return render(request, 'manager/IndexForTeacher.html')

'''def login(request):
    return render(request, 'manager/login.html')'''

def login_student(request):
    if request.method == "POST":
        user_id = request.POST.get('userid')
        password = request.POST.get('password')
        message = '请填写学号与密码！'
        if user_id.strip() and password:
            try:
                user = models.Student.objects.get(student_id=user_id)#从数据库中根据用户名检索
            except:
                message = '学号不正确！'
                return render(request, 'manager/login.html', {'message': message,'state': 'Invalid id!'})#没有这个用户就返回登录界面
            if (user.password == password): # 有的话还要检查密码是否正确
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                return redirect('login_student')
            else:
                message = '密码不正确！'
                return render(request, 'manager/login.html', {'message': 'Invalid password'})
        else:
            return render(request, 'manager/login.html', {'message': message})
    return render(request, 'manager/login.html')

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from . import models
import hashlib

def hash_code(s, salt='2.718281828'):# 加点盐
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()

Student_Login_Path='manager/login.html'
Teacher_Login_Path='manager/login_teacher.html'
Index_For_Student_Path='manager/IndexForStudent.html'
Index_For_Teacher_Path='manager/IndexForTeacher.html'

# Create your views here.
def IndexForStudent(request):
    if not request.session.get('is_login', None):#没有登录不允许访问，返回到登录页面
        return redirect("/login_student/")
    try:
        request.session.get('user_type', 'Student')#登录的账号类型不是学生也不允许访问
    except:
        return redirect('/login_student/')
    return render(request, Index_For_Student_Path)

def IndexForTeacher(request):
    if not request.session.get('is_login', None):#没有登录不允许访问，返回到登录页面
        return redirect("/login_teacher/")
    try:
        request.session.get('user_type', 'Teacher')#登录的账号类型不是老师也不允许访问
    except:
        return redirect('/login_teacher/')
    return render(request, Index_For_Teacher_Path)


def login_student(request):#学生登录
    if request.method == "POST":
        user_id = request.POST.get('userid')
        password = request.POST.get('password')
        message = '请填写学号与密码！'
        if user_id.strip() and password:
            try:
                user = models.Student.objects.get(student_id=user_id)#从数据库中根据用户名检索
            except:
                message = '学号不正确！'
                return render(request, Student_Login_Path, {'message': message,'state': 'Invalid id!'})#没有这个用户就返回登录界面
            if (user.password == password): # 有的话还要检查密码是否正确
                request.session['is_login'] = True
                request.session['user_type'] = 'Student'
                return redirect('/IndexForStudent/')
            else:
                message = '密码不正确！'
                return render(request, Student_Login_Path, {'message': 'Invalid password'})
        else:
            return render(request, Student_Login_Path, {'message': message})
    return render(request, Student_Login_Path)

def logout_student(request):#学生登出
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/login_student/")
    request.session.flush()
    return redirect("/login_student/")

def login_teacher(request):#老师登录
    if request.method == "POST":
        user_id = request.POST.get('userid')
        password = request.POST.get('password')
        message = '请填写职工号与密码！'
        if user_id.strip() and password:
            try:
                user = models.Teacher.objects.get(teacher_id=user_id)#从数据库中根据用户名检索
            except:
                message = '职工号不正确！'
                return render(request, Teacher_Login_Path, {'message': message,'state': 'Invalid id!'})#没有这个用户就返回登录界面
            if (user.password == password): # 有的话还要检查密码是否正确
                request.session['is_login'] = True
                request.session['user_type'] = 'Teacher'
                #return render(request, Index_For_Teacher_Path)
                return redirect('/IndexForTeacher/')
            else:
                message = '密码不正确！'
                return render(request, Teacher_Login_Path, {'message': 'Invalid password'})
        else:
            return render(request, Teacher_Login_Path, {'message': message})
    return render(request, Teacher_Login_Path)

def logout_teacher(request): #老师登出
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/login_teacher/")
    request.session.flush()
    return redirect("/login_teacher/")

def entrance(request):
    return render(request, 'manager/entrance.html')
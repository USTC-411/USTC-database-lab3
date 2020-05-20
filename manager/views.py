# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def IndexForStudent(request):
    return render(request, 'manager/IndexForStudent.html')

def IndexForTeacher(request):
    return render(request, 'manager/IndexForTeacher.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        message = '请填写学工号与密码！'
        if username.strip() and password:
            try:
                user_teacher = models.User.objects.get(name=username)#从数据库中根据用户名检索
            except:
                message = '用户名不正确！'
                return render(request, 'login/login.html', {'message': message,'state': 'Invalid id!'})#没有这个用户就返回登录界面
            if (user.password == password): # 有的话还要检查密码是否正确
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                return redirect('login')
            else:
                message = '密码不正确！'
                return JsonResponse({'Login state': 'Incorrect password'})
        else:
            #return render(request, 'login/login.html', {'message': message})
            return JsonResponse({'Login state': 'Empty username or password'})
    return render(request, 'manager/login.html')



# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.db.models import Q
from .. import forms
from .. import models

def campus(request):
    modify_tag = -1
    if request.GET.get('modify_tag'):
        modify_tag = request.GET.get('modify_tag')
    campus_form = forms.Campus()
    campus_modify_form = forms.Campus_modify()
    campus_set = models.Campus.objects.all()
    return render(
        request,
        'manager/ManagePage/ManageCampus.html',
        {
            'campus_set' : campus_set,
            'campus_form' : campus_form,
            'modify_tag' : modify_tag,
            'campus_modify_form' : campus_modify_form,
        }
    )

def add(request):
    if request.method == 'POST':
        add_form = forms.Campus(request.POST)
        message = 'Please check out what you write'
        if add_form.is_valid():
            campus_id = add_form.cleaned_data.get('id')
            campus_name = add_form.cleaned_data.get('name')
            campus_address = add_form.cleaned_data.get('address')
            new_campus = models.Campus(campus_id, campus_name, campus_address)
            new_campus.save()
    campus_set = models.Campus.objects.all()
    campus_form = forms.Campus()
    campus_modify_form = forms.Campus_modify()
    return render(
        request,
        'manager/ManagePage/ManageCampus.html',
        {
            'campus_set' : campus_set,
            'campus_form' : campus_form,
            'modify_tag' : -1,
            'campus_modify_form' : campus_modify_form,
        }
    )

def delete(request):
    to_be_deleted_id = request.GET.get('id');
    to_be_deleted = models.Campus.objects.get(id=to_be_deleted_id)
    message = ""
    if to_be_deleted.major.count() == 0:
        to_be_deleted.delete()
    else:
        message = "You can delete it, because it's referenced by other"
    campus_form = forms.Campus()
    campus_modify_form = forms.Campus_modify()
    campus_set = models.Campus.objects.all()
    return render(
        request,
        'manager/ManagePage/ManageCampus.html',
        {
            'campus_set' : campus_set,
            'campus_form' : campus_form,
            'modify_tag' : -1,
            'message': message,
            'campus_modify_form' : campus_modify_form,
        }
    )

def query(request):
    if  request.method == "GET":
        option = request.GET.get('option')
        query_val = request.GET.get('query_val')
        query_result = []
        if option == 'id':
            query_result = models.Campus.objects.filter(id=query_val)
        elif option == 'name':
            query_result = models.Campus.objects.filter(name=query_val)
        elif option == 'address':
            query_result = models.Campus.objects.filter(address=query_val)
        campus_form = forms.Campus()
        campus_modify_form = forms.Campus_modify()
        return render(
            request,
            'manager/ManagePage/ManageCampus.html',
            {
                'campus_set' : query_result,
                'campus_form' : campus_form,
                'modify_tag' : -1,
                'campus_modify_form' : campus_modify_form,
            }
        )

def modify(request):
    if request.method == 'POST':
        modify_form = forms.Campus_modify(request.POST)
        message = ''
        print (modify_form.errors)
        if modify_form.is_valid():
            campus_name = modify_form.cleaned_data.get('name')
            campus_address = modify_form.cleaned_data.get('address')
            tag = request.GET.get('tag')
            to_be_modified = models.Campus.objects.get(id=tag)
            # if campus_id != tag: # 如果需要修改主键
            #     message = "Cannot change the id"
            # else:
            to_be_modified.name = campus_name
            to_be_modified.address = campus_address
            to_be_modified.save()
            message = 'success'
        else:
            message = 'Please check out what you write'
    campus_set = models.Campus.objects.all()
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

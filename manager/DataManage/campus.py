# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .. import models

def campus(request):
    campus_set = models.Campus.objects.all()
    return render(request, 'manager/ManagePage/ManageCampus.html')
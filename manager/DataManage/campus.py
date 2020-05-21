# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .. import models

def campus(request):
    return render(request, 'manager/ManagePage/ManageCampus.html')
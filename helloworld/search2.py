#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.views.decorators import csrf
from django.shortcuts import render


def search_post(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, 'post.html', ctx)


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from django.http import HttpResponse
#
#
# def hello(request, name):
#     return HttpResponse('Hello %s !' % name)
#
# def hello2(request, name):
#     return HttpResponse('Hello2 %s !' % name)

from django.shortcuts import render


def hello(request, name):
    context = {}
    context['name'] = name
    return render(request, 'hello.html', context)


def hello2(request, name):
    context = {}
    context['name'] = name
    return render(request, 'hello2.html', context)

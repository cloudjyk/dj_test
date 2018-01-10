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
from django.http import HttpResponse
from django.shortcuts import render
from TestModel.models import Test


def testdb(request, name):
    conn = Test(name=name)
    conn.save()
    test1 = Test.objects.get(id=3)
    test1.name = 'Google'
    test1.save()
    Test.objects.filter(name = 'alice').update(name = 'lucy')
    Test.objects.filter(name = 'lucy').delete()
    # test1 = Test.objects.get(id=1)
    # test1.delete()
    # return HttpResponse('add username successfully')
    list = Test.objects.all().order_by('name')
    list = Test.objects.filter(id = 3).order_by('name')
    print(type(list))
    res = ''
    for i in list:
        res += '<p>' + i.name + '</p>'
    return HttpResponse('<p>' + res + '</p>')

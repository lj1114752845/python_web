# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/12/24 16:30
# @Author : 李健
# email lj2690@163.com

from django import http
import json


def default_method(request):
    return http.HttpResponse("{'name':'默认返回'}")


def get_method(request):
    assert isinstance(request, http.HttpRequest)
    student = {'name': request.GET.get('name'), 'age': request.GET.get('age')}
    student_str = json.dumps(student, ensure_ascii=False)
    return http.HttpResponse(student_str)


def post_method(request):
    assert isinstance(request, http.HttpRequest)
    student = json.loads(request.body)
    return http.HttpResponse('{"message":"收到","name"' + student['name'] + '}')

# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.utils import simplejson
from django.views.decorators.http import require_POST
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from models import UserProfile
from SEServer.lib import json_response, auth_required
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
import sys

@require_POST
@json_response
def login(request):
    '''
    required params:
        * username
        * password

    return value:
        {
            "status": 0
        }

        {
            "status": 101,
            "user_info": "用户名或密码错误"
        }

    '''
    
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(username=username,password=password)
    if user:
        if user.is_active:
            dj_login(request, user)
    else:
        return {'status': 101, 'user_info': u'bad username or password'}

    return {'status': 0}


def logout(request):
    dj_logout(request)
    return {'status': 0}

@require_POST
@auth_required
@json_response
def profile(request):
    user = request.user
    profile = request.user.profile
    if profile:
        return {
            'status': 0,
            'age': profile.age,
            'realname': profile.realname,
            'nickname': profile.nickname,
            'gender': profile.gender,
            'tags': list(profile.tags.all()),
        }
    
    return {
        'status': 104,
        'user_info': u'login required or bad profile',
    }

@require_POST
@json_response
def register(request):

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    age = request.POST.get('age', 20)
    nickname = request.POST.get('nickname', '')
    realname = request.POST.get('realname', '')
    gender = request.POST.get('gender', 0)


    user = User.objects.filter(username=username)
    if user.count() == 0:
        user = User.objects.create_user(username,'example@example.com',password)

        profile = UserProfile(**{'age':age, 'nickname':nickname, 'realname':realname, 'gender': gender})
        user.save()

        profile.user = user

        profile.save()

        user = authenticate(username=username,password=password)
        dj_login(request, user)

        return {
            'status': 0,
        }

    return {
        'status': 103,
        'user_info': u'username used',
    }

@require_POST
@auth_required
@json_response
def add_tags(request):
    user = request.user

    tags = request.POST.get('tags', None)
    if tags is None:
        return {
            'status': 103,
            'user_info': 'tags required',
        }
    tags = tags.split(',')
    user.profile.tags.add(*tags)

    r_tags = map(lambda x: x.name, user.profile.tags.all())
    print >> sys.stderr, r_tags
    return {
        'status': 0,
        'tags': r_tags,
    }

def home(request):
    return render_to_response('index.html')

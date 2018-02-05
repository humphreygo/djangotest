from django.contrib import admin      
from django.urls import path 
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import *
from blog.forms import *

from django import forms

# Create your views here.

def index(request):
    persons_list = Person.objects.all()
    
    content = {'persons_list' : persons_list}
    return render(request, 'blog/index.html', content)

def register(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()#表单数据存储到数据中
            register_info = '注册成功'
            persons_list = Person.objects.all()
            content = {'persons_list':persons_list, 'register_info':register_info}
            return render(request,'blog/index.html',content)
        else:
            return HttpResponse(form.errors)

    else:
        form = PersonForm()#表单实例化
    return render(request, 'blog/register.html',{'form':form})

def login(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            account = form.cleaned_data['account']
            passwd = form.cleaned_data['passwd']
            user = Person.objects.filter(account=account, passwd=passwd)
            if user:
                login_info = '登录成功'
                persons_list = Person.objects.all()
                content = {'persons_list':persons_list, 'login_info':login_info}
                return render(request,'blog/index.html',content)
            else:
                login_info = '登录失败'
                persons_list = Person.objects.all()
                content = {'persons_list':persons_list, 'login_info':login_info}
                return render(request,'blog/index.html',content)
    else:
        form = PersonForm()

    return render(request, 'blog/login.html',{'form':form})


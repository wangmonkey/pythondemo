#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/8/5 下午1:14 
# @Author : wangxueyang[wxueyanghj@163.com]
# @Site :  
# @File : Chapter.py 
# @Software: PyCharm
# 第二章节 变量和简单数据类型
message = "this is a message"
print(message)
message = "this is a new message"
print(message)

name = "wang xuey yang"
print(name.title())

newName = name.title();
print("the new name is ",newName)
print(newName.upper())
print(newName.lower())

old_name = "yang da xia"
cope_name = newName + " " + old_name;
print(cope_name)
print("\t",name,"\n",newName)
favorite_language = " python "
print(favorite_language)
print(favorite_language.rstrip())
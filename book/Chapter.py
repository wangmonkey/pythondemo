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

# 数字
print(2 + 3)
print(3 - 2)
print(2 * 3)
print(3 / 2)
print(3 ** 2)
print(3 ** 3)
print(10 ** 6)

print(2 + 3**4)
print((2+3)**4)

# 浮点数
print(0.1 + 0.1)
print(0.2 + 0.1)

# test
print("        ************************************               ")
print(4*2)
print(2**3)
print(16/2)
print(5+3)
print(10-2)

favorite_num = 24
favorite_num = "this is a num"
print(favorite_num)

import this
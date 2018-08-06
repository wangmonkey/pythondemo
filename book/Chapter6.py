#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/8/6 下午1:38 
# @Author : wangxueyang[wxueyanghj@163.com]
# @Site :  
# @File : Chapter6.py 
# @Software: PyCharm

alien_0 = {'color':'green','points':5}
print(alien_0['color'])
alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print("Original x-position:" + str(alien_0['x_position']))
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
# 新位置
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(alien_0)


print("********* Test ********")
person = {
    'first_name':'yang da xia',
    'last_name':'wang xue yang',
    'sex':'男',
    'city':'bei jing'
}
print(person)
del (person['sex'])
print(person)
for p in person.values() :
    print(p.title())

favorite_language = {
    "tom":"java",
    "jack":"python",
    "jerry":"C#",
    "mick":"python"
}
for language in set(favorite_language.values()):
    print(language)
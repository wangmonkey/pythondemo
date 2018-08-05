#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/8/5 下午10:38 
# @Author : wangxueyang[wxueyanghj@163.com]
# @Site :  
# @File : Chapter3.py 
# @Software: PyCharm

bicycles = ['trek','cannondale','redline','secualized']
print(bicycles)
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[-1])
print(bicycles[-2])
print("       ****************          ")
names = ["tom","jack","jerry","lucy","nike"]
print(names[1].title())
wishes = ", today is bright day"
print(names[0].title(),wishes)

names[0] = "hell"
print(names[0])
names.append("lick")
print(names)
del names[0]
print(names)
# 删除列表最后一个元素 相当于出栈
print(names.pop())
print(names)
names.remove("jerry")
print(names)

print("++++ test  +++")
names = ["xiao ming","xiao hua","zhang jun","li bin","book","anny"]
# 排序对列表的修改是永久的
names.sort()
print(names)
# 倒着打印列表  永久修改
names.reverse()
print(names)
print(names[0].title(),names[3].title(),names[2].title())
print(names[3])
names[3] = names[1]
names.pop()
print(names)
names.append("yang")
print(names)
print(names.sort())
print(len(names))
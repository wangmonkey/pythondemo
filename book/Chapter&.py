#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/8/6 下午3:19 
# @Author : wangxueyang[wxueyanghj@163.com]
# @Site :  
# @File : Chapter&.py 
# @Software: PyCharm
print("hello")
print("请输入一段信息：")
message = input("message = ")
print(message)

# 求模运算
print(4 % 3)
num = int(input("请输入用餐人数："))
if num > 9:
    print("没有空位置了")
promot = "请输入信息："
active = True
while active:
    message = input(promot)
    if message == 'quit':
        print("over")
        active = False
    else:
        print(message)
x = 1;
while x<= 5 :
    print(x)
    x += 1
    if x>3:
        break
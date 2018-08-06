#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/8/6 下午5:20 
# @Author : wangxueyang[wxueyanghj@163.com]
# @Site :  
# @File : Chapter7Test.py 
# @Software: PyCharm
responses = {}
# 设置一个标志，指出调查是否继续
polling_active = True
while polling_active:
    # 提示输入被调查者的名字和回答
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday?")
    # 将答案存储在字典中
    responses[name] = response

    # 看看是否还有人要参与调查
    repeat = input("Would you like to let another person response?(yes/no)")
    if repeat == 'no':
        polling_active = False
print("\n---  Poll Results  ---")
for name , response in responses.items():
    print(name + " would like to climb " + response + ".")
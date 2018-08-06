#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/8/6 下午5:43 
# @Author : wangxueyang[wxueyanghj@163.com]
# @Site :  
# @File : Chapter8.py 
# @Software: PyCharm
def greet_user(name):
    """ 显示简单问候语句 """
    print(" Hello !",name)
greet_user("lihua")

# 声明函数给予默认值
def getAnimalName(animal = "dog"):
    print(animal)
getAnimalName("cat")
getAnimalName()

def checkAmount(num1,num2):
    if num1 > num2:
        return "第一个数比第二个大"
    else:
        return "第一个数比第二个数小"

print(checkAmount(3,4))

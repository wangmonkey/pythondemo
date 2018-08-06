#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/8/6 上午8:53 
# @Author : wangxueyang[wxueyanghj@163.com]
# @Site :  
# @File : Chapter4.py 
# @Software: PyCharm
magicians = ['alice','david','carolina']
for magician in magicians :
    magician = "nick"
    print(magician)
print(magicians)

fruits = ['apple','banana','grape','mango']
for fruit in fruits :
    print("I like",fruit.title())
print("I really like ",fruits[1].title())

digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))
squares = [value ** 2 for value in range(1,11)]
print(squares)

a = []
for num in range(1,1000000):
    a.append(num)
print(len(a))
print(a[300:303])
print(a[-3:])

my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
print(my_foods)
print(friend_foods)
my_foods.append("cannoli")
print(my_foods)
print(friend_foods)
# 只是引用 本质上是同一个list
friend_foods = my_foods
print(friend_foods)
my_foods.append("nick")
print(friend_foods)

dimensions = (200,50)
for dimension in dimensions :
    print(dimension)

menu_foods = ("chick","vegetable","cookie")
for food in menu_foods:
    print(food)
# menu_foods[0] = "hello"
# print(menu_foods)


num1 = 2
num2 = 1
if num1>num2 and num2 < num1 :
    print("true")
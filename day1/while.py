#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/6/27 13:45
# @Author : zhouyang
# @File : while.py



# a = 1;
# while (a<2) :
#     print(a);
#     a += 1;

# 猜字游戏
import random
a = random.randint(1,10)
count = 0;
while count < 3:
    count += 1
    number = raw_input("请输入一个数字：")
    if number.isdigit():
        number = int(number)
        if number == a:
            print("猜对了")
            break;
        elif number > a:
            print("猜大了")
        elif number < a:
            print("猜小了")
        print("已用次数：",count);
    else:
        print("别闹！！！")

    if count == 3 :
        print("你的次数用完了")
        print("这个数字是：",a);
#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/6/27 下午11:46 
# @Author : wangxueyang[wxueyanghj@163.com]
# @Site :  
# @File : simple_message.py 
# @Software: PyCharm
message = "hello,world";
print("message:",message);

messages = ["hello","world","yang","da","xia"];
for m in messages:
    print(m);
messages[2] = "temp";

count = 1;
for m in messages:
    print(count," : ",m.upper());
    count += 1;
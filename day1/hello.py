# -*- coding: UTF-8 -*-
import random
def roll_dice(numbers = 3,points = None):
 print('----- 摇骰子 -----')
 if points is None:
  points = []
  # points为空列表，后续可以插入新值到该列表
 while numbers > 0:
  point = random.randrange(1,7)
  points.append(point)
  # 用append()方法将point数值插入points列表中
  numbers = numbers - 1
  # 完成一次，numbers减1，当小于等于0时不再执行该循环
 return points

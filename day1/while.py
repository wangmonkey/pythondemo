# coding=utf-8
# Python关于while循环



# a = 1;
# while (a<2) :
#     print(a);
#     a += 1;

# 猜字游戏
import random
a = random.randint(1,10)
count = 0;
while count < 3:
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

    else:
        print("别闹！！！")
    count += 1
    if count == 3 :
        print("你的次数用完了")
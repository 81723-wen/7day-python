#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Day1 聊天机器人

print('嗨，我是Day1机器人！')
name = input('你的名字：')
print(f'你好，{name}！')

age = input('你今年几岁：')
age = int(age)                #把字符串转成整数

color = input('你最喜欢的颜色：')

# 根据年龄夸一句
if age < 12:
    comment = "小朋友，python会让你更有创造力！"
elif 12 < age < 17:
    comment = "哇，青春期正是探索代码的好时候！"
elif 18 < age < 59:
     comment = '大人也可以学习代码呀！python陪你高效工作～'
else:
    comment = "这个年纪学习一点也不晚！！"

print(comment)

#把对话保存到文件
with open('day1_record.txt','w',encoding='utf-8') as f:
       f.write(f'名字：{name}\n年龄：{age}\n')
print('对话已写入 day1_record.txt,明天见！')   

# ===== 循环聊天 =====
while True:
     again = input('还想聊吗？(y/n):').strip().lower()   #去掉空格并转小写
     if again == 'y':
          name = input('你的名字：')
          age  = int(input('你今年几岁：'))
          print(f'嗨，{name},{age}岁，很高兴再次见面！')
     elif again == 'n':
            print('拜拜，明天继续加油学python！')
            break       #退出循环
     else:
        print('请输入 y 或者 n 哦。')
   


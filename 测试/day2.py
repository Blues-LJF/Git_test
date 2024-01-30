# from random import randint
# import random
# print(randint(1, 100))
# print(random.random())
#!/usr/bin/python3
# coding: utf-8
from random import randint


def randomAnser(answer):
    
    while True:
        number = int(input('请输入: '))
        if number < answer:
            print('大一点')
        elif number > answer:
            print('小一点')
        else:
            print('恭喜你猜对了!')
            break

randomAnser(randint(1, 100))

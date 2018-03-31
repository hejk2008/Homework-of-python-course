#! /usr/bin/env python3
# coding: utf-8

from math import pi

def int_part(x):
    return len(str(int(x)))

def main():
    while 1:
        try:
            radius = float(input('Radius? '))
            break
        except ValueError:      #当检测到实数以外的字符时，提示用户重新输入
            print('Please input a real number.')
    area = pi * radius ** 2
    print('Area is:',area)      #输出面积
    print('Its integral part is a %d-digit number.'%int_part(area))       #计算整数的位数

if __name__ == '__main__':
    main()


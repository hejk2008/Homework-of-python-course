#! /usr/bin/env python3
# coding:utf-8

def main():
    score = eval(input('Score?'))
    if score>100:
        print('Error!')
    elif score>=90:
        print('A')
    elif score>=85:
        print('A-')
    elif score>=82:
        print('B+')
    elif score>=78:
        print('B')
    elif score>=75:
        print('B-')
    elif score>=71:
        print('C+')
    elif score>=66:
        print('C')
    elif score>=62:
        print('C-')
    elif score>=60:
        print('D')
    elif score>=0:
        print('F')
    else:
        print('Error!')


if __name__ == '__main__':
    main()

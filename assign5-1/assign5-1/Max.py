#! /usr/bin/env python3
# coding:utf-8

def main():
    firstnum = input('The 1st number is: ')
    secondnum = input('The 2nd number is: ')
    if eval(firstnum)<eval(secondnum):
        firstnum, secondnum = secondnum , firstnum
    print('the bigger one is: ' + firstnum)


if __name__ == '__main__':
    main()
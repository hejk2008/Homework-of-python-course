#! /usr/bin/env python3
# coding:utf-8

def main():
    n = int(input('请输入n：'))
    for i in range(1,n+2):
        print(' '*(n+1-i)*2 + '* '*(2*i-1))
    for i in range(n,0,-1):
        print(' '*(n+1-i)*2 + '* '*(2*i-1))


if __name__ == '__main__':
    main()

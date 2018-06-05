#! /usr/bin/env python3
#coding:utf-8

def main():
    word = input('请输入：')
    for i in range(len(word)-1,0,-1):
        output = ' '.join((word[:i], word[i:]))
        print(output)
    print('-'*5)
    for i in range(1,len(word)):
        output = ' '.join((word[:i], word[i:]))
        print(output)


if __name__ == '__main__':
    main()

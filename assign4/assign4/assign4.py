#! /usr/bin/env python3
# coding:utf-8

'''
    宋词自动生成器
'''

def main():
    '''10个词语版本主程序'''
    mapping = {'0':'江南', '1':'春风', '2':'憔悴', '3':'多情', '4':'为谁',
               '5':'匆匆', '6':'归去', '7':'相思', '8':'回首', '9':'依旧'}
    num = input('请输入一串数字：')
    for i in num:
        print(mapping.get(i), end='')


if __name__ == '__main__':
    main()

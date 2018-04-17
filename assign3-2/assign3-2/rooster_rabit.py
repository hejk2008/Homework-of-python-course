#! /usr/bin/env python3
# coding:utf-8


def main():
    try:
        head = int(input('共有多少头？'))
        foot = int(input('共有多少脚？'))
        if foot < head *2 or foot > head * 4 or head <= 0 or foot <= 0 or foot%2 == 1:  #排除不可能的数字组合
            print('No answer.')
        else:
            answer = [(rooster, rabbit) for rooster in range(head+1) for rabbit in range(head+1)
                      if (head == rooster+rabbit and foot == rooster*2 + rabbit*4)]
            print('鸡：%d\n兔：%d'%(answer[0]))
    except ValueError:      #避免输入数字以外的字符报错
        print('Please input a number.')


if __name__ == '__main__':
    main()

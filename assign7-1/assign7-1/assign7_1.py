#! /usr/bin/env python3
#coding:utf-8

def main():
    words = input('请输入两个单词，以空格分割：').split(sep=' ')
    word1 = words[0]
    word2 = words[1]
    if set(word1) == set(word2):
        print('单词%s与%s是相似词！'%(word1, word2))
    else:
        print('单词%s与%s不是相似词！'%(word1, word2))


if __name__ == '__main__':
    main()
    
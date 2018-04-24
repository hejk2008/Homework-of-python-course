#! /usr/bin/env python3
# coding:utf-8

'''
    宋词自动生成器附加题
'''

def csvtodict(filename, coding='utf-8'):
    '''将csv文件转换为字典'''
    with open(filename, 'r', encoding=coding, errors='ignore') as file:
        dictdata = file.read().replace('\n', ',')
    dictlist = tuple(dictdata.split(','))
    return dict(zip(dictlist[::2], dictlist[1::2]))


def digitstopoem(numberstr, dictionary):
    '''将数字转化为诗句'''
    if len(numberstr) % 2 == 1:
        numberstr = numberstr[:-1]
    poem = ''
    for i in range(0, len(numberstr), 2):
        poem = poem.join(dictionary.get(numberstr[i:i+2]))
    return poem


def main():
    '''100个词语版本主程序'''
    try:
        numstr = input('请输入数字序列：')
        int(numstr)     #用于在输入整数之外的字符时报错
        dikt = csvtodict('dict100words.csv', 'cp936')
        print(digitstopoem(numstr, dikt))
    except FileNotFoundError:
        print('请确认已从eLearning下载运行所需的字典：dict100words.csv')
    except ValueError:
        print('请输入数字！')


if __name__ == '__main__':
    main()

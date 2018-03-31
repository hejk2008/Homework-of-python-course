#! /usr/bin/env python3
# coding:utf-8

import math

#产生1个0~99的列表
a=list(range(0,100))

#你能写出几种让列表元素逆序排列的方法（结果仍存放在a中）？答案写在下面。
a.sort(reverse=1)
a = sorted(a,reverse=1)
a.reverse()
a = list(reversed(a))
a = a[::-1]


#重新排序
a.sort()

#利用切片得到a中从21开始的所有奇数,存放在列表b中。答案写在下面。
b = a[21::2]

#利用列表推导式，得到a中所有的质数,存放在列表c中。答案写在下面。
c = [p for p in a[2:] if 0 not in [p%d for d in range(2,int(math.sqrt(p))+1)]]

#利用列表推导式，得到a中所有能被2或3整除的数,存放在列表d中。答案写在下面。
d = [i for i in a if(i%2 == 0 or i%3 == 0)]





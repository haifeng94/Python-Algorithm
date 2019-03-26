# coding=utf-8

'''
题目：我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
'''

'''
斐波那契数列
2*n的大矩形，和n个2*1的小矩形
其中 2*n为大矩阵的大小
有以下几种情形：
1.n <= 0 大矩形为<= 2*0,直接return 0
2.n = 1大矩形为2*1，只有一种摆放方法，return 1
3.n = 2 大矩形为2*2，有两种摆放方法，return 2
4.target = n 分为两步考虑：
第一次摆放一块 2*1 的小矩阵，则摆放方法总共为f(n - 1)
√
√
第一次摆放一块1*2的小矩阵，则摆放方法总共为f(n-2)
因为，摆放了一块1*2的小矩阵（用√√表示），对应下方的1*2（用××表示）摆放方法就确定了，所以为f(n-2)
√	√
×	×
n >= 3  f(n) = f(n - 1) + f(n-2)
'''


class Solution:
    def retCover(self, number):
        if number <= 0:
            return 0
        elif number < 3:
            return number
        else:
            a = 1
            b = 2
            while number >= 3:
                a, b = b, a+b
                number -= 1
            return b

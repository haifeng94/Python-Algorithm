# coding=utf-8

'''
题目：求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字有1、
10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出
任意非负整数区间中1出现的次数。
'''

#方法一：常规方法
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        count = 0
        for i in range(1, n+1):
            for j in str(i):
                if j == '1':
                    count += 1

        return count


#方法二: 获取每个位数区间上所有数中包含1的个数，然后分别对高位分析，然后递归的处理低位数
#http://www.cnblogs.com/qiaojushuang/p/7780445.html

def get_digits(n):
    #求整数n的位数
    ret = 0
    while n:
        ret += 1
        n /= 10
    return ret


def get_1_digits(n):
    """
    获取每个位数之间1的总数
    :param n: 位数
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    current = 9 * get_1_digits(n-1) + 10 ** (n-1)
    return get_1_digits(n-1) + current


def get_1_nums(n):
    if n < 10:
        return 1 if n >= 1 else 0
    digit = get_digits(n)  # 位数
    low_nums = get_1_digits(digit-1)  # 最高位之前的1的个数
    high = int(str(n)[0])  # 最高位
    low = n - high * 10 ** (digit-1)  # 低位

    if high == 1:
        high_nums = low + 1  # 最高位上1的个数
        all_nums = high_nums
    else:
        high_nums = 10 ** (digit - 1)
        all_nums = high_nums + low_nums * (high - 1)  # 最高位大于1的话，统计每个多位数后面包含的1
    return low_nums + all_nums + get_1_nums(low)
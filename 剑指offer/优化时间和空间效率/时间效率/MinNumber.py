# coding=utf-8

'''
题目：输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''

'''
将输入数组转成字符串，利用cmp比较mn或者nm的大小，进行从小到大的排序
'''

from functools import cmp_to_key

def cmp(a,b):#Python2
    return int(str(a)+str(b)) - int(str(b) + str(a))   #两两进行比较，大于0就交换位置，这样就可以把"合并"后小的放到前面

class Solution:
    def PrintMinNumber(self, nums):
        if not nums:
            return ''
        return ''.join([str(num) for num in sorted(nums, key=cmp_to_key(lambda a, b: int(str(a)+str(b)) - int(str(b) + str(a))))])
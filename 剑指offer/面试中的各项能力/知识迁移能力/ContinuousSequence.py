# coding=utf-8

'''
要求：输入一个正数s， 打印出所有和为s的正整数序列(至少两个数)
思路: 使用两个指针，和比s小，大指针后移，比s大，小指针后移
'''

class Solution:
    def FindContinuousSequence(self, tsum):
        if tsum < 3:
            return []
        a, b = 1, 2
        ret = []
        while a < s//2 + 1:
            if sum(range(a,b+1)) == tsum:
                ret.append(list(range(a, b+1)))
                a += 1
            elif sum(range(a, b+1)) < tsum:
                b += 1
            else:
                a += 1

        return ret
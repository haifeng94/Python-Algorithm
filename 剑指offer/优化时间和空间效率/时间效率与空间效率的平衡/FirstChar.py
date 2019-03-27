# coding=utf-8

'''
题目：在一个字符串(1<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置
'''

'''
思路一：先遍历一遍字符串，用一个hash表存放每个出现的字符和字符出现的次数。再遍历一遍字符串，找到hash值等于1的输出即可。
思路二：利用python函数的特性
'''

class Solution:
    def FirstNotRepeatingChar(self, s):
        if not s:
            return -1

        count = {}
        for i in s:
            if i not in count.keys():
                count[i] = 0
            count[i] += 1

        for j in s:
            if count[j] == 1:
                return s.index(j)

        return -1

class Solution2:
    def FirstNotRepeatingChar2(self, s):
        if not s:
            return -1

        for i in s:
            if s.count(i) == 1:
                return s.index(i)

        return -1
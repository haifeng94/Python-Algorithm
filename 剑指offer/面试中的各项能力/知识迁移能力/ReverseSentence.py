# coding=utf-8

'''
要求：翻转一个英文句子中的单词顺序，标点和普通字符一样处理
思路: Python中字符串是不可变对象，不能用书中的方法，可以直接转化成列表然后转回去
'''

class Solution:
    def ReverseSentence(self, s):
        if not s:
            return ''
        return ' '.join(s.split()[::-1])

s = 'student. a am I'
sl = Solution()
res = sl.ReverseSentence(s)
print(res)
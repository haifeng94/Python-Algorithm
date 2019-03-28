# coding=utf-8

'''
题目：求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
'''

'''
思路一：利用了python的特性, range和sum
'''

class Solution:
    def Sum_Solution(self, n):
        return sum(range(1, n+1))

s = Solution()
res = s.Sum_Solution(5)
print(res)

'''
思路二：其实跟思路一差不多
'''
class Solution2:
    def Sum_Solution2(self, n):
        from functools import reduce
        return reduce(lambda x, y: x+y, range(1, n+1))

s2 = Solution2()
res = s2.Sum_Solution2(5)
print(res)
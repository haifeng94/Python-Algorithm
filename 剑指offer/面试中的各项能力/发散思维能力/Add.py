# coding=utf-8

'''
题目：写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
'''

'''
思路一：用sum函数，但是特别注意sum()求和里面是个[]列表对象，直接输入num，num2是不行的
'''

class Solution:
    def add(self, num1, num2):
        return sum([num1, num2])


'''
思路二：使用位运算，Python中大整数会自动处理，因此对carry需要加个判断
'''

class Solution2:
    def add2(self, num1, num2):
        while num2:
            #异或运算相当于只求和不进位
            s = num1 ^ num2
            #与操作，并向左移一位，相当于求进位
            carry = (num1 & num2) << 1
            num1 = s
            num2 = carry

        return num1

s = Solution2()
res = s.add2(1000000,200000)
print(res)
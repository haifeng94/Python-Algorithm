#coding = utf-8
'''
题目：大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
思路：
F = 0                            -->  n = 0
F = 1                            -->  n = 1
F(n) = F(n-1) + F(n-2)           -->  n >= 2
'''

def fib(n):
    a, b = 0, 1
    while n > 0:
        print(b)
        a, b = b, a+b
        n -= 1

fib(10)
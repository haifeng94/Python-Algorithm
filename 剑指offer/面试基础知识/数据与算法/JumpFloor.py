#coding = utf-8
'''
题目：一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

思路：
        | 1               (n=1)
f(n) =  | 2               (n=2)
        | f(n-1)+f(n-2)   (n>2,n为整数)
'''

def fib(n):
    a, b = 1, 2
    while n > 0:
        print(b)
        a, b = b, a+b
        n -= 1

fib(10)

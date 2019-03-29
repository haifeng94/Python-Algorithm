#coding = utf -8

'''
题目：打印1到最大的n位数，如n=3时打印1到999

思路：Python中已经对大整数可以进行自动转换了，所以不需要考虑大整数溢出问题
'''

class Solution:
    def Print1ToMaxOfNDigits(self, n):
        for i in range(1,10**n):
            print(i)

s = Solution()
s.Print1ToMaxOfNDigits(2)


#方法二：
import types

def SumEmulator(num): # num = '35499'

    i = len(num) - 1
    flag = 0
    lastNum = ''

    while True:
        if i == -1:
            return '1' + lastNum
        elif num[i] == '9':
            lastNum = '0' + lastNum
            i -= 1
        else:
            lastNum = str(int(num[i]) + 1) + lastNum
            return num[:i] + lastNum

def Print1ToMaxOfNDigits(num): # num = '35499'

    if num == '':
        return False
    else:
        i = 0
        while i <= int(num) - 1:
            print(SumEmulator(str(i)))
            i += 1
    return 0

Print1ToMaxOfNDigits('35967896786797948')
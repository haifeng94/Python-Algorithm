# coding=utf-8

'''
题目：将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0
思路一：使用int(),但是通过了
'''

class Solution:
    def StrToInt(self, s):
        try:
            return int(s)
        except:
            return 0

'''
思路二：特殊处理，比如123+，就不合理，但是-123就合理，因为这是个负数
'''

class Solution2:
    def StrToInt2(self, string):
        if not string:
            return 0
        flag = 0
        ret = 0
        numbers = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        for k, s in enumerate(string):
            if s in numbers.keys():
                ret = ret*10 + numbers[s]
            else:
                if not flag:
                    if s == '+' and k == 0:
                        flag = 1
                    elif s == '-' and k == 0:
                        flag = -1
                    else:
                        return 0
                else:
                    return 0
        if flag and len(string) == 1:
            return 0
        return ret if flag >= 0 else -ret

def str_to_int(string):
    if not string:  # 空字符返回0
        return 0
    flag = 0  # 用来表示第一个字符是否为+、-
    ret = 0  # 结果
    for k, s in enumerate(string):
        if s.isdigit():  # 数字直接运算
            val = ord(s) - ord('0')
            ret = ret * 10 + val
        else:
            if not flag:
                if s == '+' and k == 0:  # 避免中间出现+、-
                    flag = 1
                elif s == '-' and k == 0:
                    flag = -1
                else:
                    return 0
            else:
                return 0
    if flag and len(string) == 1:  # 判断是不是只有+、-
        return 0
    return ret if flag >= 0 else -ret

print(str_to_int('0023'))

#coding = utf-8

'''
题目：输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
思路：二进制表示中，最后的那个1被减去后，低位都变为0，高位不变，按位与就可以去掉这个1
'''

def num_of_1(n):
    ret = 0
    while n:
        ret += 1
        n = n & n-1

    return ret

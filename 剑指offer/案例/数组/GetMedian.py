#coding = utf -8

'''
题目：如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
'''

'''
思路一：常规操作
'''

class Solution:
    def __init__(self):
        self.array = []

    def Insert(self, num):
        self.array.append(num)
        sorted(self.array)

    def getMedian(self, M):
        length = len(self.array)
        if length % 2 == 1:
            return self.array[length // 2]
        return (self.array[length // 2] + self.array[length // 2 - 1]) / 2.0
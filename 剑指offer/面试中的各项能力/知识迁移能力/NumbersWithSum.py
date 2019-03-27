# coding=utf-8

'''
要求：输入一个递增排序的数组和一个数字s，在数组中查找两个数，使其和为s
思路: 设置头尾两个指针，和大于s，尾指针减小，否砸头指针增加
'''

class Solution:
    def FindNumbersWithSum(self, array, tsum):
        if len(array) < 2:
            return []
        head, end = 0, len(array)-1
        while head < end:
            if array[head] + array[end] == tsum:
                return [array[head], array[end]]
            elif array[head] + array[end] > tsum:
                end -= 1
            else:
                end += 1

        return []

s = Solution()
res = s.FindNumbersWithSum([1,2,3,4,5,6,7], 7)
print(res)
# coding=utf-8

'''
题目：数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。\

思路：列表的len方法的时间复杂度是O(1)
'''

class Solution:
    def get_more_than_half_num(self, nums):
        hashes = dict()
        length = len(nums)
        for n in nums:
            hashes[n] = hashes[n] + 1 if hashes.get(n) else 1
            if hashes[n] > length / 2:
                return n
        return 0

'''
题目：输入一个链表，输出该链表中倒数第k个结点。
思路：使用列表的切片，还是很快的
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        if k > len(res) or k < 1:
            return
        return res[-k]
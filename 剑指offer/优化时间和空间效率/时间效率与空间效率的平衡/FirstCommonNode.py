#coding = utf -8

'''
题目：输入两个链表，找出它们的第一个公共结点
'''

'''
思路一：
第一种情况：相同长度有交点
两个指针一起走，步长一致，碰到第一个相同的节点 p1 == p1，退出循环，return p1。
第二种情况：相同长度无交点
两个指针一起走，直到走到最后一个节点，p1.next 和 p2.next都为 None，满足 相等的条件，退出循环，return p1。
第三种情况：不同长度有交点
两个指针一起走，当一个指针p1走到终点时，说明p1所在的链表比较短，让p1指向另一个链表的头结点开始走，直到p2走到终点，让p2指向短的链表的头结点，那么，接下来两个指针要走的长度就一样了，变成第一种情况。
第四种情况：不同长度无交点
两个指针一起走，当一个指针p1走到终点时，说明p1所在的链表比较短，让p1指向另一个链表的头结点开始走，直到p2走到终点，让p2指向短的链表的头结点，那么，接下来两个指针要走的长度就一样了，变成第二种情况。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if not pHead1 or not pHead2:
            return None
        p1, p2 = pHead1, pHead2
        while p1 != p2:
            p1 = pHead2 if not p1 else p1.next
            p2 = pHead1 if not p2 else p2.next

        return p1

'''
思路二：从后往前找第一个不公共的，所以可以用栈来做呀～～全部入栈，然后同时出栈，直到不相等为止就行
'''

class Solution2:
    def FindFirstCommonNode(self, pHead1, pHead2):
        stack1 = []
        stack2 = []
        while pHead1:
            stack1.append(pHead1)
            pHead1 = pHead1.next
        while pHead2:
            stack2.append(pHead2)
            pHead2 = pHead2.next
        pre = None
        while stack1 and stack2 and stack1[-1] == stack2[-1]:
            pre = stack1.pop()
            stack2.pop()

        return pre

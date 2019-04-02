#coding = utf -8

'''
题目：在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#思路一
class Solution:
    def deleteDuplication(self, pHead):
        first = ListNode(-1)
        first.next = pHead
        last = first

        while pHead and pHead.next:
            if pHead.val == pHead.next.val:
                val = pHead.val
                while pHead and val == pHead.val:
                    pHead = pHead.next
                last.next = pHead
            else:
                last = pHead
                pHead = pHead.next

        return first.next

#思路二：将链表里面所有的数存在一个列表里面，然后把列表里面只出现一次的数提取出来，在新建一个链表放进去
class Solution2:
    def deleteDuplication(self, pHead):
        res = []
        while pHead:
            res.append(pHead.val)
            pHead = pHead.next

        #filter函数和map相似，但是filter是返回布尔值去去输入列表进行判断
        res = list(filter(lambda c: res.count(c) == 1, res))

        newlist = ListNode(0)
        pre = newlist
        for i in res:
            node = ListNode(i)
            pre.next = node
            pre = pre.next

        return newlist.next
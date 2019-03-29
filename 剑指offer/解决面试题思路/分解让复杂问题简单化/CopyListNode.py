#coding = utf -8

'''
题目：输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
'''

'''
思路：1. 根据旧链表创建新链表，不去管随机的那个指针
     2. 根据旧链表中的随机指针，创建新链表中的随机指针
     3. 从旧链表中拆分得到新链表
'''

class RandomListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None

class Solution:
    #返回RandomListNode
    def Clone(self, pHead):
        if pHead == None:
            return None
        self.CloneNodes(pHead)
        self.ConnectRandomNodes(pHead)

        return self.ReconnectNodes(pHead)

    #复制原始链表的每个结点, 将复制的结点链接在其原始结点的后面
    def CloneNodes(self, pHead):
        pNode = pHead
        while pNode:
            pClone = RandomListNode(0)
            pClone.val = pNode.val
            pClone.next = pNode.next
            pNode.next = pClone
            pNode = pClone.next

    #将复制后的链表中的复制结点的random指针链接到被复制结点random指针的后一个结点
    def ConnectRandomNodes(self,pHead):
        pNode = pHead
        while pNode:
            pClone = pNode.next
            if pNode.random != None:
                pClone.random = pNode.random.next

            pNode = pClone.next

    #拆分链表, 将原始链表的结点组成新的链表, 复制结点组成复制后的链表
    def ReconnectNodes(self, pHead):
        pNode = pHead
        pCloneHead = pCloneNode = pNode.next
        pNode.next = pCloneHead.next
        pNode = pNode.next

        while pNode:
            pCloneNode.next = pNode.next
            pCloneNode = pCloneNode.next
            pNode.next = pCloneNode.next
            pNode = pNode.next

        return pCloneHead
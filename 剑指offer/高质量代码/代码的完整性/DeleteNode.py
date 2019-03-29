#coding = utf -8

'''
题目：给定单链表的头指针和一个结点指针，定义一个函数在O(1)时间删除节点。

思路：因为已经给了要删除节点的指针，可以找到待删除节点的写一个节点的值，复制到待删除节点，将该节点的next指针指向next.next就行了，流程如下:
(1) a->b->c->d->e 要删除的是c节点
(2) a->b->d->d->e 将待删除节点的下一个节点的值复制到该节点
(3) a->b->d   d->e 将待删除节点的next指向它的next.next

                |          ^

                |_____|
'''

#初始化单链表
#class Node(object):
#    def __init__(self, val, p=0):
#        self.val = val
#        self.next = p

class Solution:
    def deleteNode(self, listHead, deleteNode):
        if listHead == deleteNode:                      #只有一个结点
            listHead = listHead.next
        elif deleteNode.next == None:                   #要删除节点为尾节点
            while listHead:
                if listHead.next == deleteNode:
                    listHead.next = None
                listHead = listHead.next
        else:                                           #要删除节点是中间节点
            deleteNode.val = deleteNode.next.val
            deleteNode.next = deleteNode.next.next
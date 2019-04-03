#coding = utf -8

'''
题目：一个链表中包含环，请找出该链表的环的入口结点。
'''

#思路一：字典, 缺点：空间复杂度O(N)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def entryNodeOfLoop(self, pHead):
        dic = {}
        dic[pHead] = 1
        while dic[pHead] != 2 and pHead.next:
            pHead = pHead.next
            if pHead not in dic:
                dic[pHead] = 1
            else:
                return pHead
        return None

'''
思路二：
1. 分别用oneStep，twoStep指向链表头部，oneStep每次走一步，twoStep每次走二步，直到oneStep==twoStep找到二者在环中的相汇点。
2. 当oneStep==twoStep时，twoStep所经过节点数为2x,oneStep所经过节点数为x,设闭环中有n个节点,twoStep比oneStep多走k圈有2x=kn+x; nk=x;
简单起见，可以看作k=1，oneStep实际走了一个环的步数，再让twoStep指向链表头部，oneStep位置不变，oneStep,twoStep每次走一步直到oneStep==twoStep; 此时oneStep指向环的入口。
'''

class Solution2:
    def entryNodeOfLoop(self, pHead):
        if pHead == None or pHead.next == None:
            return None
        oneStep = pHead
        twoStep = pHead
        while twoStep and twoStep.next:
            oneStep = oneStep.next
            twoStep = twoStep.next.next
            if oneStep == twoStep:
                oneStep = pHead
                while oneStep != twoStep:
                    oneStep = oneStep.next
                    twoStep = twoStep.next
                return oneStep

        return None

#关于有环没环的更多介绍，https://zhuanlan.zhihu.com/p/31401474
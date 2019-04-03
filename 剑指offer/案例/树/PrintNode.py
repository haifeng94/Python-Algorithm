#coding = utf -8

'''
题目：请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，
第三行按照从左到右的顺序打印，其他行以此类推。
'''

'''
思路： 转换思路，存储的时候一直从左向右存储，打印的时候根据不同的层一次打印
'''

#class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    def Print(self, pRoot):
        if not pRoot:
            return []
        nodes, res, flag = [pRoot], [], True
        while nodes:
            curStack, nextStack = [], []
            for node in nodes:
                curStack.append(node.val)
                if node.left:
                    nextStack.append(node.left)
                if node.right:
                    nextStack.append(node.right)
            #整的是一级的curStack的顺序了，不是二级的nextStack的顺序
            if not flag:
                curStack.reverse()
            if curStack:
                res.append(curStack)
            nodes = nextStack
            flag = not flag

        return res
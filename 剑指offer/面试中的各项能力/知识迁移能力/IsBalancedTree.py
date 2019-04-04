#coding = utf -8

'''
题目：输入一棵二叉树，判断该二叉树是否是平衡二叉树。
平衡二叉树：它是一棵空树或它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树。
'''

#class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    def IsBalanced_Solution(self, pRoot):
        self.flag = True
        self.tree_Iteration(pRoot)
        return self.flag

    def tree_Iteration(self, pRoot):
        if not pRoot or self.flag == False:
            return 0
        left = self.tree_Iteration(pRoot.left)
        right = self.tree_Iteration(pRoot.right)
        if abs(right-left) > 1:
            self.flag = False
        return left+1 if left>right else right+1

# coding=utf-8

'''
题目：输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
'''

'''
思路：由于输入的一个二叉搜索树，其左子树大于右子树的值，这位后面的排序做了准备，因为只需要中序遍历即可，将所有
的节点保存到一个列表，。对这个list[:-1]进行遍历，每个节点的right设为下一个节点，下一个节点的left设为上一个节点。
二叉搜索树：又名二叉查找树，左孩子比父节点小，右孩子比父节点大，还有一个特性就是”中序遍历“可以让结点有序。
中序遍历：左根右
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return
        self.attr = []
        self.midOreder(pRootOfTree)
        for i, v in enumerate(self.attr[:-1]):
            v.right = self.attr[i+1]
            self.attr[i+1].left = v
        return self.attr[0]

    def midOreder(self, root):
        if not root:
            return
        self.midOreder(root.left)
        self.attr.append(root)
        self.midOreder(root.right)

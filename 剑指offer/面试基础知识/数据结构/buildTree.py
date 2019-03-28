#coding=utf-8
'''
题目：用前序和中序遍历结果构建二叉树，遍历结果中不包含重复值
思路：前序的第一个元素是根结点的值，在中序中找到该值，中序中该值的左边的元素是根结点的左子树，右边是右子树，然后递归的处理左边和右边
'''

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder)==0:
            return None
        
        root=TreeNode(preorder[0])
        middle=inorder.index(preorder[0])
        root.left=self.buildTree(preorder[1:middle+1],inorder[:middle])
        root.right=self.buildTree(preorder[middle+1:],inorder[middle+1:])
        return root

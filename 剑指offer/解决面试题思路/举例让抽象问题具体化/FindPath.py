# -*- coding:utf-8 -*-

'''
题目：输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
'''

'''
思路：
递归先序遍历树， 把结点加入路径。使用列表结构存树结构
若该结点是叶子结点则比较当前路径和是否等于期待和，叶子节点说明该路径应该截止了
弹出结点，每一轮递归返回到父结点时，当前路径也应该回退一个结点。
'''

def find_path(tree, num):
    res = []
    if not tree:
        return res
    path = [tree]
    sums = [tree.val]

    def dfs(tree):
        if tree.left:
            path.append(tree.left)
            sums.append(sums[-1] + tree.left.val)
            dfs(tree.left)
        if tree.right:
            path.append(tree.right)
            sums.append(sums[-1] + tree.right.val)
            dfs(tree.right)
        if not tree.left and not tree.right:
            if sums[-1] == num:
                res.append([p.val for p in path])
        path.pop()
        sums.pop()

    dfs(tree)
    return res
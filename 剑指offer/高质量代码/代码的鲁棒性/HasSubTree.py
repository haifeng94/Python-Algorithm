
'''
题目：输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
思路：分为两步：第一步在树A中找到和B的根结点的值一样的结点R，第二步再判断树A中以R为根节点的子树是不是包含和树B一样的结构
'''

#方法一
def sub_tree(tree1, tree2):
    if tree1 and tree2:
        if tree1.val == tree2.val:
            return sub_tree(tree1.left, tree2.left) and sub_tree(tree1.right, tree2.right)
        else:
            return sub_tree(tree1.left, tree2) or sub_tree(tree1.right, tree2)

    if not tree1 and tree2:
        return False

    return True

# coding=utf-8

class Node():
    '''节点'''
    def __init__(self, elem, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

class Tree():
    '''二叉树'''
    def __init__(self, root=None):
        self.root = root

    def add(self, elem):
        node = Node(elem)
        if self.root == None:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            while queue:
                cur = queue.pop(0)
                if cur.lchild == None:
                    cur.lchild = node
                    return
                elif cur.rchild == None:
                    cur.rchild = node
                    return
                else:
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)

    def preorder(self, root):
        '''深度优先——先序遍历：根节点->左子树->右子树'''
        if root == None:
            return
        print(root.elem)
        self.preorder(root.lchild) #递归
        self.preorder(root.rchild)

    def inorder(self, root):
        '''深度优先——中序遍历：左子树->根节点->右子树'''
        if root == None:
            return
        self.inorder(root.lchild) #递归
        print(root.elem)
        self.inorder(root.rchild)

    def postorder(self, root):
        '''深度优先——后序遍历：左子树->右子树->根节点'''
        if root == None:
            return
        self.postorder(root.lchild)
        self.postorder(root.rchild)
        print(root.elem)

    def breadth_travel(self, root):
        '''广度优先———层次遍历：利用队列实现'''
        if root == None:
            return
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            print(node.elem)
            if node.lchild != None:
                queue.append(node.lchild)
            if node.rchild != None:
                queue.append(node.rchild)

if __name__ == "__main__":
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)

    #先序遍历
    tree.preorder(tree.root)
    #中序遍历
    tree.inorder(tree.root)
    #后续遍历
    tree.postorder(tree.root)
    #广度优先
    tree.breadth_travel(tree.root)

# coding=utf-8

class Node(object):
    '''节点'''
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

class Tree(object):
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
        '''深度优先——先序遍历：根节点->左子树->右子树---栈实现'''
        if root == None:
            return
        stack = []
        cur = self.root
        while cur or stack: #利用栈实现树的先序遍历
            while cur:  #从根节点开始，一直找它的左子树
                print(cur.elem)
                stack.append(cur)
                cur = cur.lchild
            cur = stack.pop() #while结束时表示当前节点node为空，即前一个节点没有左子树了
            cur = cur.rchild  #开始查看它的右子树

    def inorder(self, root):
        '''深度优先——中序遍历：左子树->根节点->右子树---栈实现'''
        if root == None:
            return
        stack = []
        cur = self.root
        while cur or stack:
            while cur:  #从根节点开始，一直找它的左子树
                stack.append(cur)
                cur = cur.lchild
            cur = stack.pop()  #while结束表示当前节点node为空，即前一个节点没有左子树了
            print(cur.elem)
            cur = cur.rchild   #开始查看它的右子树

    def postorder(self, root):
        '''深度优先——后序遍历：左子树->右子树->根节点---栈实现'''
        if root == None:
            return
        stack1 = []
        stack2 = []
        cur = self.root
        stack1.append(cur)
        while stack1: #这个while循环的功能是找出后序遍历的逆序，存在myStack2里面
            cur = stack1.pop()
            if cur.lchild:
                stack1.append(cur.lchild)
            if cur.rchild:
                stack1.append(cur.rchild)
            stack2.append(cur)
        while stack2:
            print(stack2.pop().elem) #将myStack2中的元素出栈，即为后序遍历次序

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
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)

    #先序遍历
    #tree.preorder(tree.root)
    #中序遍历
    #tree.inorder(tree.root)
    #后续遍历
    tree.postorder(tree.root)
    #广度优先
    #tree.breadth_travel(tree.root)

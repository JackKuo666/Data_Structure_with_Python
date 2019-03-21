# _*_ coding: UTF-8 _*_
"""二叉树

"""
# 通过使用Node类中定义三个属性，分别为elem本身的值，还由左右子树
class Node(object):
    """节点类"""
    def __init__(self, elem = -1, lchild = None, rchild = None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

# 树的创建，创建一个树的类，并给一个root根节点，一开始为空，随后添加节点
class Tree(object):
    """树类"""
    def __init__(self, root = None):
        self.root = root

    def add(self, elem):
        """为树添加节点"""
        node = Node(elem)
        # 如果树是空的，则对根节点赋值
        if self.root is None:
            self.root = node
            return
        else:
            queue = []
            queue.append(self.root)
            # 对已有节点进行层次遍历
            while queue:
                # 弹出队列的第一个元素
                cur = queue.pop(0)
                if cur.lchild == None:
                    cur.lchild = node
                    return
                elif cur.rchild == None:
                    cur.rchild = node
                    return
                else:
                    # 如果左右子树都不为空，加入队列继续判断
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)

# ×××××××××    深度优先遍历  ××××××××××××××××××
    def preorder(self, root):
        """递归实现先序遍历"""
        if root == None:
            return
        print(root.elem, end= " ")
        self.preorder(root.lchild)
        self.preorder(root.rchild)

    def inorder(self, root):
        """递归实现中序遍历"""
        if root == None:
            return
        self.inorder(root.lchild)
        print(root.elem, end= " ")
        self.inorder(root.rchild)

    def postorder(self, root):
        """递归实现后续遍历"""
        if root == None:
            return
        self.postorder(root.lchild)
        self.postorder(root.rchild)
        print(root.elem, end= " ")

# ××××××××××    广度优先遍历   ×××××××××
    # 从树的root开始，从上到下从从左到右遍历整个树的节点
    def breadth_travel(self):
        """利用队列实现树的层次遍历"""
        if self.root == None:
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.elem, end= " ")
            if node.lchild != None:
                queue.append(node.lchild)
            if node.rchild != None:
                queue.append(node.rchild)



if __name__ == "__main__":
    t = Tree()
    for i in range(10):
        t.add(i)
    t.breadth_travel()
    print("\n")
    t.preorder(t.root)
    print("\n")
    t.inorder(t.root)
    print("\n")
    t.postorder(t.root)


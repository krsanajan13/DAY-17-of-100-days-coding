class Node:
    def __init__(self,val):
        self.val=val
        self.right=None
        self.left=None

class BSTree:
    def __init__(self):
        self.root=None

    def insertNode(self,node,val):
        n=Node(val)
        if self.root==None:
            self.root=n
            return
        if val<node.val:
            if node.left==None:
                node.left=n
            else:
                self.insertNode(node.left,val)
        else:
            if node.right==None:
                node.right=n
            else:
                self.insertNode(node.right,val)
b=BSTree()
b.insertNode(None,10)
b.insertNode(b.root,5)


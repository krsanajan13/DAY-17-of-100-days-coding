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

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.val, end=" ")
            self.inorder(node.right)

    # DFS: Preorder Traversal (Root, Left, Right)
    def preorder(self, node):
        if node:
            print(node.val, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    # DFS: Postorder Traversal (Left, Right, Root)
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.val, end=" ")
b=BSTree()
b.insertNode(None,10)
b.insertNode(b.root,5)
b.insertNode(b.root, 15)
b.insertNode(b.root, 3)
b.insertNode(b.root, 7)
print("\nInorder DFS: ")
b.inorder(b.root)

print("\nPreorder DFS: ")
b.preorder(b.root)    

print("\nPostorder DFS: ")
b.postorder(b.root)


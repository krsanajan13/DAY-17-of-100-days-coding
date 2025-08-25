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

    def bfs(self):
        if not self.root:
            return
        queue = [self.root]  # using list instead of deque
        while queue:
            current = queue.pop(0)  # remove first element
            print(current.val, end=" ")
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
b=BSTree()
b.insertNode(None,10)
b.insertNode(b.root,5)
b.insertNode(b.root, 15)
b.insertNode(b.root, 3)
b.insertNode(b.root, 7)
print("BFS Traversal: ")
b.bfs()



class Node:
    def __init__(self,val):
        self.val=val
        self.prev=None
        self.next=None

class DLL:
    def __init__(self):
        self.root=None
        self.tail=None

    def addNewNode(self,val):
        n=Node(val)

        if self.root is None:
            self.root=n
            self.tail=n
            return
        self.tail.next=n
        n.prev=self.tail
        self.tail=n

    def display(self):
        temp=self.root
        while temp != None:
            print(temp.val,end=' ')
            temp=temp.next



d=DLL()
d.addNewNode(10)
d.addNewNode(20)
d.addNewNode(30)
d.addNewNode(40)
d.addNewNode(50)
d.display()


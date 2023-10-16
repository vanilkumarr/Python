class BST:
    def __init__(self,key):
        self.key=key
        self.right=None
        self.left=None

    def insert(self,data):
        if self.key is None:
            self.key=data
            return
        if self.key > data: 
            if self.left:
                self.left.insert(data)
            else:
                self.left=BST(data)
        else:

            if self.right:
                self.right.insert(data)
            else:
                self.right=BST(data)
    def search(self,data):
        if self.key == data:
            print("Node is found")
            return
        if self.key > data: 
            if self.left:
                self.left.search(data)
            else:
                print("Node is not present")
        else:
            if self.right:
                self.right.search(data)
            else:
                print("node is not prresmt")
    def delete(self,data,curr):
        if self.key == None:
            print("treee is empty ")
            return
        if self.key > data:
                if self.left:
                    self.left=self.left.delete(data)
                else:
                    print("no data")
        elif self.key < data:
            if self.right:
                self.right=self.right.delete(data)
            else:
                print("no data")
        else:
            if self.left is None:
                temp=self.right
                if data == curr:
                    self.key = temp.key
                    self.left= temp.left
                    self.right= temp.right
                    temp=None
                    return
                self=None
                return temp
            if self.right is None:
                temp=self.left
                if data == curr:
                    self.key = temp.key
                    self.left= temp.left
                    self.right= temp.right
                    temp=None
                self=None
                return temp
            node=self.right
            while node.left:
                node=node.left
            self.key=node.key
            self.right=self.right.delete(node.key,curr)
        return self    
         
    def pre_order(self):
        print(self.key)
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()
    def in_order(self):
        if self.left:
            self.left.in_order()
        print(self.key)
        if self.right:
            self.right.in_order()
    def post_order(self):
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()
        print(self.key)
    def min(self):
        temp=self
        while temp.left:
            temp=temp.left
        print(temp.key)
    def max(self):
        temp=self
        while temp.right:
            temp=temp.right
        print(temp.key)

    def display(self):
        if self.left:
            self.left.display()
        print(self.key)
        if self.right:
            self.right.display()
def count(node):
    if node is None:
        return 0
    return 1+count(node.left)+count(node.right)
roots=BST(10) 
list1=[3,7,7,3,3,3,11,35454,2,11,22]
for i in list1:
    roots.insert(i)
if count(roots) >1: 
    roots.delete(10,roots.key)
else:
    print("cant delete the node")
roots.max()
roots.min()

            


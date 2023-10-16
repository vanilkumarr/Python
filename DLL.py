class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DLL:
    def __init__(self):
        self.head=None
    def insert_begining(self):
        new=Node(input())
        new.next=self.head
        self.head=new
    def insert_end(self):
        new1=Node(input())
        temp=self.head
        while temp.next != None:
            temp=temp.next
        temp.next=new1
        new1.prev=temp.next
    def insert_betweeen(self):
        new=Node(input("insert at middle"))
        pos=int(input("Enter the position "))
        temp=self.head
        for i in range(pos):
            temp=temp.next
        temp.next=new
        new.prev=temp

    def deletion_first(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        self.head.prev=None
    def deletion_end(self):
        temp=self.head.next
        before=self.head
        while temp.next != None:
            temp=temp.next
            before=before.next
        before.next=None
        temp.prev=None
    def deletion_mid(self):
        pos=2
        temp=self.head
        
        for i in range(pos):
            temp=temp.next
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        print("deleted")
        temp.prev=None
        temp.next=None

    def display(self):
        if self.head ==None:
            print("empty list")
        else:
            temp=self.head                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    

            while temp:
                print(temp.data,'++>',end ="")
                temp=temp.next
l=DLL()
n1=Node(10)
l.head=n1
n2=Node(20)
n1.next=n2
n1.prev=l.head
n3=Node(30)
n2.next=n3
n2.prev=n1
n3.prev=n2
l.insert_begining()
'''l.insert_betweeen()
l.insert_end()
l.deletion_first()
l.deletion_end()


'''
l.deletion_mid()
l.display()
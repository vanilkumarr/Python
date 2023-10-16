class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:
    def __init__(self):
        self.head=None

    def insert_at_begin(self):
       new= Node(input("enter begin"))
       new.next = self.head
       self.head=new
    def insert_at_end(self):
        newed=Node(input("enter emd"))
        temp=self.head

        while temp.next != None:
            temp=temp.next
        temp.next=newed
    def insertanywhere(self):
        naw=Node(23)
        pos=3
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        naw.next=temp.next
        temp.next=naw
    def deletion_fisrt(self):
        self.head=self.head.next


    def deletion_last(self):
        temp=self.head.next
        prev=self.head
        while temp.next !=None:
            temp=temp.next
            prev=prev.next
        prev.next=None
    def deletion_mid(self):
        temp=self.head.next
        prev=self.head
        pos=3
        for i in range(1,pos-1):
            temp=temp.nexts
            prev=prev.next
        prev.next=temp.next
        temp.next=None

    def display(self):
        if self.head == None:
            print("list is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data,'==>',end=" ")
                temp = temp.next


l = SLL()
n1= Node(input("enter N1"))
l.head=n1
n2=Node(input("enter N2"))
n1.next=n2
n3=Node(input("enter N3"))
n2.next=n3
l.insert_at_begin()
l.insert_at_end()
l.insertanywhere()
l.deletion_fisrt()
l.deletion_last()
l.deletion_mid()
l.display()




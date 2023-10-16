class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Cll:
    def __init__(self):
        self.head=None
    def insert_begining(self):
        new=Node(0)
        if self.head == None:
            new.next=new
        temp=self.head
        while temp.next != self.head:
            temp= temp.next
        temp.next=new
        new.next=self.head
        self.head=new
    def insert_end(self):
        new=Node(50)
        if self.head == None:
            new.next=new
        else:
            temp=self.head
            while temp.next != self.head:
                temp=temp.next
            temp.next=new
            new.next=self.head
    def insert_between(self):
        pos=3
        new=Node(40)
        if self.head == None:
            new.next=new
        else:
            temp=self.head
            for i in range(pos-1):
                temp=temp.next
            new.next=temp.next
            temp.next=new
    def deletion(self):
        temp=self.head
        while temp.next != self.head:
            temp=temp.next
        self.head=self.head.next
        temp.next=self.head 

    def deletion_end(self):
        temp=self.head.next
        before=self.head
        while temp.next != self.head:
            temp = temp.next
            before=before.next
        before.next = self.head

    def deletion_mid(self):
        pos=1
        temp=self.head.next
        before=self.head
        for i in range(pos-1):
            temp=temp.next
            before=before.next
        before.next=temp.next
        temp.next=None
    def searching(self):
        temp = self.head
        ele = 40
        count = 0
        while True:
            if ele == temp.data:
                count += 1
            temp = temp.next
            if temp == self.head:
                break
        print(count)



            

    def display(self):
        if self.head == None:
            print("empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"++>",end="")
                temp=temp.next
                if temp == self.head:
                    break
l=Cll()
n1=Node(10)
l.head=n1
n1.next=l.head

n2=Node(20)
n1.next=n2
n2.next=l.head
l.insert_begining() 
l.insert_end()
l.insert_between()
l.searching()
l.display()



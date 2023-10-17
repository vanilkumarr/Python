def insertionsort(mylist):
    for i in range(1,len(mylist)):
        element=mylist[i]
        pos=i
        while element<mylist[pos-1] and pos>0:
            mylist[pos]=mylist[pos-1]
            pos=pos-1
        mylist[pos]=element
list1=[98,143,68,0,2,22]
insertionsort(list1)
print(list1)

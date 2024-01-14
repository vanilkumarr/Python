def insertionsort(mylist):
    for i in range(1,len(mylist)):
        element=mylist[i]
        while element<mylist[i-1] and i>0:
            mylist[i]=mylist[i-1]
            i=i-1
        mylist[i]=element
list1=[98,143,68,0,2,22]
insertionsort(list1)
print(list1)



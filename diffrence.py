list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7]
i=0
list=[]
while len(list1)>i:
    if list1[i] not in list2:
        a=list1[i]
        list.append(a)
    i=i+1
print(list)

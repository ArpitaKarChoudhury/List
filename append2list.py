list1=[[10, 20], [30, 40], [50, 60], [30, 20, 80]]
list2=[[61], [12, 14, 15], [12, 13, 19, 20], [12]]
a=0 
while a<len(list1):
    b=0
    while b<len(list2[a]):
        list1[a].append(list2[a][b])
        b=b+1
    a=a+1
print(list1)
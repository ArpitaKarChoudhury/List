list=[6,1,3,5,1,3,6]
a=0
b=[]
c=1
while a<len(list):
    if list[a] not in b:
        b.append(list[a])
        c=c*b[a]
    a=a+1
print(c)
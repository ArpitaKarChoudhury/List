list=[2,32,4,5,6,13,10]
a=0
b=0
while a<len(list):
    if b<list[a]:
        b=list[a]        
    a=a+1
list.remove(b)
i=0
j=0
while i<len(list):
    if j<list[i]:
        j=list[i]
    i=i+1
list.remove(j)
k=0
p=0
while k<len(list):
    if p<list[k]:
        p=list[k]
    k=k+1
list.remove(p)
print("max no=",b,",","second max no=",j,",","third max no=",p)
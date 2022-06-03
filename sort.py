l=[1,3,7,4,3,4,5,9]
i=0
while i<len(l):
    a=i+1
    while a<len(l):
        if l[i]>l[a]:
            k=l[i]
            l[i]=l[a]
            l[a]=k
        a=a+1 
    i=i+1    
print(l)
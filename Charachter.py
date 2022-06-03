#[[2,'a'],[2,'b'],'c',[2,'d'],'e','f',[2,'g'],'h']
a="aabbcdddefggh"
b=0
z=[]
while b<len(a):
    z.append(a[b])
    b=b+1
print(z)
b=0
e=[]
while b<len(z):
    c=1+b
    sum=1
    d=[]
    while c<len(z):
        if z[b]==z[c]:
            sum=sum+1
            d.append(sum)
            d.append(z[b])
            e.append(d)
        if z[b]!=z[c]:
            break        
        c=c+1    
    b=b+2
print(e)
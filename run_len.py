a=[1, 1, 2,3,4,4,5,1]
b=0
e=[]
while b<len(a):
    c=1+b
    sum=1
    d=[]
    while c<len(a):
        if a[b]==a[c]:
            sum=sum+1
            d.append(sum)
            d.append(a[b])
            e.append(d)
        if a[b]!=a[c]:
            break
        c=c+1
    e.append(a[c])
    b=b+2
print(e)
a=[2,2,3,4,4,5,5,5,5,2,6,7,8,8]
b=0
e=[]
while b<len(a):
    global sum
    c = b+1
    d=[]
    sum=1
    while c<len(a):
        if a[b] == a[c]:
            sum=sum+1
        c=c+1
    if sum>1:
        d.append(a[b])
        d.append(sum)
        e.append(d)
    else:
        e.append(a[b])
    b=b+sum
print(e)

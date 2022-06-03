number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19]
a=0
g=[]
while len(n)>a:
    b=a+1
    while len(n)>b:
        d=[]
        c=n[a]+n[b]
        if number==c:
            e=n[a]
            f=n[b]
            d.append(e)
            d.append(f)
            g.append(d)
        b=b+1    
    a=a+1   
print(g)
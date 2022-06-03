
a=input("enter number")
b=len(a)
c=0
d=[]
while c<len(a):
    d.append(a[c])
    c=c+1
print(d)
e=0
while e<len(d):
    if int(d[e])>0:
        f=d[e]+"0"*(len(d)-(e+1))
        print(f+"+",end="")
    e=e+1
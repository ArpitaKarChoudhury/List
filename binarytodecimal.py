a=[1,0,0,1,1]
b=a[::-1]
i=0
d=0
while i<len(b):
    if b[i] ==1:
        c=b[i]*2**i
        d=c+d
    i=i+1
print(d)

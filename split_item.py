list=['Red', 'Maroon', 'Yellow', 'Olive']
a=0
d=[]
while a<len(list):
    b=0
    c=[]
    while b<len(list[a]):
        
        c.append(list[a][b])
        b=b+1
    d.append(c)
    a=a+1
print(d)
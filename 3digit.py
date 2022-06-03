# Given 3 digits a, b, and c. The task is to find all the possible combinations from these digits.
# Examples:
# Input: [1, 2, 3]
# Output:
# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1
list=[1,2,3]
a=0
z=[]
while a<len(list):
    b=0
    c=[]
    c.append(list[a])
    while b<len(list):
        if list[b] not in c:
            c.append(list[b])
        b=b+1
    x=1
    y=[]
    while x<len(list):
        if list[x] not in y:
            y.append(list[x])
        x=x+1
    if list[a] not in y:
        y.append(list[a])
    re=0-len(y)
    re1=-1
    g=[]
    while re1>=re:
        if y[re1] not in g:
            g.append(y[re1])
        re1=re1-1
    b=0-len(c)
    d=-1
    e=[]
    while d>=b:
        if c[d] not in e:
            e.append(c[d])
        d=d-1        
    a=a+1
    if c not in z:
        z.append(c)
    if e not in z:
        z.append(e)
    if y not in z:
        if len(y)==3:
            z.append(y)
    if g not in z:
        if len(g)==3:
            z.append(g)
print(z)
a="9 1 1 9"
b=0
c=" "
e=a.split(' ')
print(e)
while b<len(e):
    d=int(e[b])**2
    c=c+str(d)
    b=b+1
print(c)


# list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list=[2,4,6,8]
a=0
b=a
d=[]
while a<len(list):
    b=a+1
    while b<len(list):
        if list[a]<list[b]:
            c=list[b]-list[a]
            d.append(c)
        break
        b=b+1
    a=a+1
print(d)
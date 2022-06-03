list = [1, 2, 2, 5, 8, 4, 4, 8]
a=0
b=[]
c=0
while a<len(list):
    if list[a] not in b:
        b.append(list[a])
        c=c+1
    a=a+1
print(b)
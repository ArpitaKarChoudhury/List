# For statues = [6, 2, 3, 8], the output should be
# makeArrayConsecutive2(statues) = 3.
list= [6,4,2,3,8]
a=0
c=[]
while a<len(list):
    b=a
    while b<len(list):
        if list[a]>list[b]:
            k=list[a]
            list[a]=list[b]
            list[b]=k
        b=b+1
    a=a+1
print(list)
a=0
while a<len(list):
    b=int(list[a])+1
    c=a+1
    while c<len(list):
        if b not in list:
            list.insert(c,b)
            break
        c=c+1
    a=a+1
print(list)
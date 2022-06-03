# Original list:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Difference between elements (n+1th - nth) of the said list :
# [1, 1, 1, 1, 1, 1, 1, 1, 1]
# Original list:
# [2, 4, 6, 8]
# Difference between elements (n+1th - nth) of the said list :
# [2, 2, 2]
list=[1,2,3,4,5,6,7,8,9,10]
a=0
d=[]
while a<len(list):
    b=a+1
    while b<len(list):
        c=int(list[b])-int(list[a])
        d.append(c)
        if b==a+1:
            break
        b=b+1
    
    a=a+1
print(d)
list=[2,4,6,8]
a=0
d=[]
while a<len(list):
    b=a+1
    while b<len(list):
        c=int(list[b])-int(list[a])
        d.append(c)
        if b==a+1:
            break
        b=b+1
    
    a=a+1
print(d)

# Write a Python program to pair up the consecutive elements of a given list.Original lists:
# [1, 2, 3, 4, 5, 6]
# Pair up the consecutive elements of the said list:
# [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
# Original lists:
# [1, 2, 3, 4, 5]
# Pair up the consecutive elements of the said list:
# [[1, 2], [2, 3], [3, 4], [4, 5]]
list=[1,2,3,4,5,6,7]
a=0
d=[]
while a<len(list):
    b=a+1
    c=[]
    while b<len(list):
        c.append(list[a])
        c.append(list[b])
        d.append(c)
        b=b+1
        break   
    a=a+1
print(d)
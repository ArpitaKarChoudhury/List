# #Write a Python program to find the list with maximum and minimum length.
# Original list:
# [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# List with maximum length of lists:
# (3, [13, 15, 17])
# List with minimum length of lists:
# (1[0])
list=[[0,9],[0,2,2],[1,3,3,9,9],[5,3,3,7],[4,8,811],[2,8,17]]
a=0
c=0
while a<len(list):
    b=0
    while b<len(list[a]):
        d=len(list[a])
        if c<d:
            c=d
            e=list[a]
        b=b+1
    d=0
    while d<len(list[a]):
        f=len(list[a])
        g=len(list[d])
        if g<f:
            i=g
            h=list[d]
        d=d+1
    a=a+1
print("maximum is",c,e)
print("minimum is",i,h)
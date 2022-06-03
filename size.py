# Original list:
# [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
list=[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
a=0
z=int(input("enter number"))
e=[]
while a<len(list):
    c=[]
    d=a
    b=a+z
    while d<len(list):
        if d<b:
            c.append(list[d])
        d=d+1
    e.append(c)
    a=a+z
print(e)
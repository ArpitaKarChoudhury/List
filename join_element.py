# Write a Python program to join adjacent members of a given list.
# Original list:
# ['1', '2', '3', '4', '5', '6', '7', '8']
# Join adjacent members of a given list:
# ['12', '34', '56', '78']
# Original list:
# ['1', '2', '3']
# Join adjacent members of a given list:
# ['12']
list = ['1', '2', '3', '4', '5', '6', '7', '8','9']
a=0
d=[]
while a<len(list):
    b=a+1
    while b<len(list):
        c=list[a]+list[b]
        d.append(c)
        break
        b=b+1
    a=a+2
print(d)

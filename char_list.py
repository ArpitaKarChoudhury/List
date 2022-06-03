# Write a Python program to iterate a given list cyclically on specific index position.
# Original list:
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# Iterate the said list cyclically on specific index position 3 :
# ['d', 'e', 'f', 'g', 'h', 'a', 'b', 'c']
# Iterate the said list cyclically on specific index position 5 :
# ['f', 'g', 'h', 'a', 'b', 'c', 'd', 'e']
list=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
a=int(input("enter number"))
b=a-len(list)
print(b)
c=[]
while b>=0-len(list):
    c.append(list[b])
    b=b-1
a=a+1
while a<len(list):  
    c.append(list[a])
    a=a+1
print(c)
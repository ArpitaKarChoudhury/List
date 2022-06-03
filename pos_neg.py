# Given a list of numbers, write a Python program to count positive and negative numbers in a List.
# Example:
# list1 = [2, -7, 5, -64, -14]
# Output: pos = 2, neg = 3
list1 = [2, -7, 5, -64, -14]
a=0
pos=0
neg=0
while a<len(list1):
    if list1[a]>0:
        pos=pos+1
    elif list1[a]<0:
        neg=neg+1
    a=a+1
print("pos=",pos,"neg=",neg)
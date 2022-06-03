# Write a Python program to remove the last N number of elements from a given list.
# Original lists:
# [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]
# Remove the last 3 elements from the said list:
# [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34]
# Remove the last 5 elements from the said list:
# [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34]
# Remove the last 1 element from the said list:
# [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3]
list=[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]
a=0
b=int(input("enter number"))
c=len(list)-b
d=[]
while a<len(list):
    if a<c:
        d.append(list[a])
    a=a+1
print(d)

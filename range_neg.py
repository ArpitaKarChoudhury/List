# Given the start and end of a range, write a Python program to print all negative numbers in a given
# range.
# Example:
# Input: start = -4, end = 5
# Output: -4, -3, -2, -1
# Input: start = -3, end = 4
# Output: -3, -2, -1
a=int(input("enter number"))
b=int(input("enter number"))
while a<b:
    if a==0:
        break
    print(a,end=" ")
    a=a+1
# Write a Python program to check if first digit/character of each element in a given list
# is same or not.
# Original list:
# [1234, 122, 1984, 19372, 100]
# Check if first digit in each element of the said given list is same or not!
# True
# Original list:
# [1234, 922, 1984, 19372, 100]
list1 = [1234, 122, 1984, 19372, 100]
# list1=["a",'aabc', 'abc', 'ab', 'a']
a=0
b=0
while a<len(list1):
    list=str(list1[a])
    c=0
    list2=str(list1[c])
    if list[b] != list2[b]:
        f="false"
        print(f)
        break
    a=a+1
else:
    print("true")
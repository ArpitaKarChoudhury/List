# Remove duplicates from a list.
list = [1,2,3,1,2,2]
# # Output: [1,2,3]
a=0
b=[]
while a<len(list):
    if list[a] not in b:
        b.append(list[a])
    a=a+1
print(b)
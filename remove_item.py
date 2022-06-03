# Input :
# 1 1 2 3 4 5 1 2
# 1
# Output :2 3 4 5 2
# Explanation : The input list is [1, 1, 2, 3, 4, 5, 1, 2] and the item to be removed is 1.
# After removing the item, the output list is [2, 3, 4, 5, 2]
# Input :
# 5 6 7 8 9 10
# 7
# Output :
# 5 6 8 9 10
list=[1,1,2,3,4,5,1,2]
k=1
a=0
b=[]
while a<len(list):
    if k!=list[a]:
        b.append(list[a])        
    a=a+1
print(b)
# Given a List, extract all elements whose frequency is greater than K.
# Input: test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3
# Output: [4, 3]
# Explanation: Both elements occur 4 times.
# Input: test_list = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6], K = 2
# Output: [4, 3, 6]
# Explanation: Occur 4, 3, and 3 times respectively.
list = [4, 5, 5, 5, 3,3,3,8,8]
k = 2
a=0
c=[]
while a<len(list):
    b=a+1
    sum=0
    while b<len(list):
        sum=sum+1
        if list[a]==list[b] and k<=sum:
            d=list[a]
            if d not in c:
                c.append(d)  
        b=b+1
    a=a+1
print(c)
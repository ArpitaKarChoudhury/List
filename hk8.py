# Given an array nums of distinct integers, 
# return all the possible permutations. 
# You can return the answer in any order
nums = [1,2,3]
a=0
e=[]
while a<len(nums):
    b=a+1
    while b<len(nums):
        c=nums[a]
    e.append(b)
    a=a+1
print(e)    
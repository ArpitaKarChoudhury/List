# Find the sum of number digits in List.
# The original list is :[12, 67, 98, 34] 
# List Integer Summation : [3, 13, 17, 7]
# Explanation: 1+2 = 3, 6+7=13, 9+8=17, 3+4=7
# The original list is : [15, 81, 11, 234]List Integer Summation : [6,9,2,9]
list=[12, 67, 98, 349]
a=0
while a<len(list):
    b=0
    c=str(list[a])
    while b<len(c):
        d=str(c)
        e=0
        f=0
        while e<len(d):
            f=int(d[e])+f
            e=e+1
        b=b+1
    print(f,end=", ")
    a=a+1
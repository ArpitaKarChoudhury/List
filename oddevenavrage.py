elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
a=0
sum=0
sum1=0
b=0
b1=0
while a<len(elements):
    if elements[a]%2==0:
        b=b+1
        sum=sum+elements[a]
    elif elements[a]%2!=0:
        b1=b1+1
        sum1=sum1+elements[a]
    a=a+1
print("odd numbers",sum1//b1,"even numbers",sum//b)
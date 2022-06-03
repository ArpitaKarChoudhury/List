money = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
a=0
b=0
c=0
d=0
while a<len(money):
    
    if money[a]>=1000000:
        b=b+1
        # print(a+1,"-crorepati")
    elif money[a]>=100000:
        c=c+1
        # print(a+1,"-lakhpati")
    else:
        d=d+1
        #  print(a+1,"-dilwale")
    a=a+1
print("crorepati is",b,"lakhpati is",c,"dilwale is",d)
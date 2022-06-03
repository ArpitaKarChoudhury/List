marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]]
a=0
while len(marks)>a:
    b=0
    sum=0
    while len(marks[a])>b:
        sum =sum+marks[a][b]
        b=b+1
    print(sum//len(marks[a]))
    a=a+1

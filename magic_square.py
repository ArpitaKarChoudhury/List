magic_square=[[8,3,4],[1,5,9],[6,7,2]]
i=0
while i<len(magic_square):
    j=0
    row=0
    while j<len(magic_square[i]):
        row =row +magic_square[i][j]
        j=j+1
    print(row)
    i=i+1
b=0
c=0
col=0
while c<len(magic_square):
    while b<len(magic_square[c]):
        col=col+magic_square[c][b]
        b=b+1
    print(col)
    c=c+1
a=0
b=0
dig=0
while a<len(magic_square):
    while b<len(magic_square):
        if a==b:
            c=magic_square[a][b]
            dig=dig+c
            break
        b=b+1
    a=a+1
print(dig)
a=0
b=0
dig2=0
c=len(magic_square[a])-1
while len(magic_square)>a:
    while len(magic_square[a])>b:
        if a==b:
            c=magic_square[a][b]
            dig2=dig2+c
            break
        b=b+1
    a=a+1
print(dig2)
if row==col and dig==dig2:
    print("it is a magic square")
else:
    print("it is not a magic square")

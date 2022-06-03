latters=[['g','f','g'],['i','s'],['b','e','s','t']]
a=0
while a<len(letters):
    b=0
    while b<len(letters[a]):
        c=letters[a][b]
        print(c,end="")
        b=b+1
    a=a+1
print()
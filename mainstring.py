mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
subStr = "over"
b=mainStr.split()
a=0
while a<len(b):
    if subStr!=b[a]:
        print(b[a],end=" ")
    a=a+1
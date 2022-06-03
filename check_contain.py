list1="https://www.w3resource.tv"
list2=['.com', '.edu', '.tv']
a=0
while a<len(list2):
    if list2[a] in list1:
        print("true")
        break
    a=a+1
else:
    print("false")
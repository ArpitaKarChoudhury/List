# Original lists:
# ['0', '1', '2', '3', '4']
# ['red', 'green', 'black', 'blue', 'white']
# ['100', '200', '300', '400', '500']
# Concatenate element-wise three said lists:
# ['0red100', '1green200', '2black300', '3blue400', '4white500']
list=['0', '1', '2', '3', '4']
list1=['red', 'green', 'black', 'blue', 'white']
list2=['100', '200', '300', '400', '500']
a=0
b=" "

while a<len(list):
    d=[]
    b=b+list[a]+list1[a]+list2[a]
    a=a+1
d.append(str(b))
print(d)
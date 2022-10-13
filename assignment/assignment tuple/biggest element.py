#biggest element in list and print position.

list=[1,3,5,10,2,88,7,5,66,42,99]
largest=0
new=[]
for i in list:
    if i>largest:
        new.append(i)
        largest=i
print('largest=',largest)
print(new)
print('largest=',new[-1])
print('index=',list.index(largest))
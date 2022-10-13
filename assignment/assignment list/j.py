#Remove multiple elements from a list in Python

list1=['apple','boy','cat','dog','cat','apple','boy','boy','frog','goat','cat']
list2=[]
for i in list1:

    if i in list2:
        continue
    else:
        list2.append(i)
print(list2)






#Python – Adding Tuple to List and vice – versa

a=(1,2)
b=('a','b','c')
c=('k','l')
list1=[]
list1.append(a)
list1.append(b)
list1.append(c)

print(list1)

#list+tuple

list2=['apple','boy','cat','dog']
list2+=a

list2+=b
list2+=c
print(list2)
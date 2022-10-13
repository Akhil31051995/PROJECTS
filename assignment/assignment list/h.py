
#Python program to count Even and Odd numbers in a List

list2=[1,2,3,5,4,6,9,8,7,11,13,17,55,44]
counteven=countodd=0
for i in list2:
    if i%2==0:
        counteven+=1
    else:
        countodd+=1

print('count of odd=',countodd)
print('count of even=',counteven)

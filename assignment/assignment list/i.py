#Python program to print positive numbers in a list
#Python program to print negative numbers in a list
#Python program to count positive and negative numbers in a list


list1=[-1,-2,-3,-4,-5,10,23,8,-7,-99,85]
pos=[]
neg=[]
countpos=0
countneg=0
for i in list1:
    if i<0:
        neg.append(i)
        countneg+=1
    else:
        pos.append(i)
        countpos+=1

print('positive no=',countpos)
print('negative no=',countneg)
print('positive nos=',pos)
print('negative nos=',neg)

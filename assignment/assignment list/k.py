#Python program to print all positive numbers in a range
#Python program to print all negative numbers in a range

first=int(input('enter starting no'))
last=int(input('enter the last no '))
neg=[]
pos=[]

for i in range(first,last+1):

    if i<0:
        neg.append(i)
    elif i==0:
        continue
    else:
        pos.append(i)


print('positive list=',pos)
print('negative list=',neg)
#Python Program to find sum and average of List in Python

#Python | Sum of number digits in List
#Python | Multiply all numbers in the list

num=[23,45,6,8,9,4]
sum=0
product=1
for i in num:
    sum=sum+i
    product=product*i
print('sum=', sum)
print('average=',sum/len(num))
print('product=', product)
#Python program to find smallest number in a list

#Python program to find largest number in a list

#Python program to find second largest number in a list


list1=[45,8,6,9,7,45,62,78,5,20,77,63]
#print(max(list1))     using min max function

list1.sort()
largest=list1[-1]
smallest=list1[0]
secondlargest=list1[-2]

print('smallest=',smallest)
print('largest=',largest)
print('secondlargest=',secondlargest)
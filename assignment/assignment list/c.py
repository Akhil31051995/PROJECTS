#Maximum of two numbers in Python

#Minimum of two numbers in Python


num1=int(input('enter first no'))
num2=int(input('enter second no'))

new=[num1,num2]
new.sort()

print('minimum',new[0])
print('maximum',new[-1])
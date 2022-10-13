#Write a program named to print the decimal part.the decimal part of a number.
# If decimal part is zero function should return this string: "INTEGER".

a=float(input('enter the correct number?'))
b=int(a)
x=a-b

if x==0:
    print('INTEGER')
else:
    print('the decimal part of the number is', x)
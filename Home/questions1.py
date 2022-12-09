# 8 write a program to print the reverse of a number [use while loop]
# num=1234
# n=str(num)
# i=len(n)-1
# new=' '
# while i>=0:
#     new+=n[i]
#     i-=1
#
# print(new)



# 12 write a program to find whether the given number is an armstrong number or not [use while loop]

# num=input('enter the number:')
# i=0
# l=[]
# while i<len(num):
#     l.append((int(num[i]))**(len(num)))
#     i+=1
# if sum(l)==int(num):
#     print('armstrong number:',num)
# else:
#     print('not an armstrong number')
#
# print(l)



# construct following pattern using nested loop:
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# for i in range(10):
#     if i<5:
#         print('*'*i)
#     if i>=5:
#         print('*'*((9-i)))


#1 List comprehensions:
# (a) Generate positive list of numbers from a given list of integers
# (b) Square of N numbers
# (c) Form a list of vowels selected from a given word
# (d) Form a list ordinal value of each element of a word (Hint: use ord() to get ordinal
# values)

# l=[2,3,0,1,-7,-8,5,-9]
# pos=[ i  for i in l if i>0]
# print(pos)

# l=[2,3,0,1,-7,-8,5,-9]
# sq=[i**2 for i in l]
# print(sq)


# vow=[i for i in input('enter the word:') if i in 'aeiouAEIOU']
# print(vow)

# ordi=[ord(i) for i in input('enter the word:')]
# print(ordi)



#2 Merge two dictionaries.

# a={'a':1,'b':2}
# b={'c':5,'d':8}
#
# a.update(b)
# print(a)

# 7 display the given pyramid with the step number accepted from the user, E.g, N=4
# 1
# 2 4
# 3 6 9
# 4 8 12 16









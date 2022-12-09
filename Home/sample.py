#write a program to prompt the user for list of numbers ,for all values greater than 100 store 'over' instead
l=input('enter the numbers:')

num=[int(i)  if int(i)<=100 else 'over' for i in l.split(",") ]

print(num)


# l=[]
# for i in input('enter the nos:').split(','):
#     if int(i)<=100:
#         l.append(int(i))
#     else:
#         l.append('over')
#
# print(l)
#
#
# l=[]


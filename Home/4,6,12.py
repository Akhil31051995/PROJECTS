# 6.Write a program to prompt the user to enter two list of integers and check
#
# #check wheter list of same length
# #wheter the list sums to same value
# #wheter any value occurs in both lists
#
# 12. from a list of integers create a list after removing even numbers
#
# 14.Add 'ing' to the end of a given string,if it already ends with 'ing' then add 'ly'



# list1=[int(i) for i in input('enter the nos:').split(' ')]
# list2=[int(i) for i in input('enter the second list:').split(' ')]
# print(list1)
# print(list2)
#
# if len(list1)==len(list2):
#     print('length same')
# if sum(list1)==sum(list2):
#     print('sum same')
#
# common=[i for i in list1 if i in list2]
# print(common)


# integer=[1,2,3,5,6,4,7,8,9,77,88,56,44,20]
# oddlist=[i for i in integer if i%2!=0 ]
#
# print(oddlist)


string=input('enter the string:')
if 'ing' in string:
    print(string+'ly')
else:
    print(string+'ing')


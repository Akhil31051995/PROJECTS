#Python program to swap two elements in a list

#Python – Swap elements in String list

list1=['apple','mango','banana','plum','jackfruit','grapes','avocado','orange']

pos1=int(input('enter the first index'))
pos2=int(input('enter the second index'))
#list2=list1.copy()


a=list1[pos1]      #storing the string in first position to a new variable 'a' to enter it later
b=list1[pos2]       ##storing the string in second position to a new variable 'b' to enter it later

list1[pos1]=b
list1[pos2]=a


print(list1)